"""
PDF Converter module.

This module provides the main class for converting PDF files to JSONL format.
"""

import os
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Union

from src.config.pdf_converter_config import PDFConverterSettings
from .pdf_reader import PDFReader
from .pdf_parser import PDFParser
from .json_converter import JSONConverter
from .jsonl_writer import JSONLWriter
from .text_corrector import TextCorrector

logger = logging.getLogger(__name__)


class PDFConverter:
    """Main class for converting PDF files to JSONL format."""

    def __init__(self, settings: Optional[PDFConverterSettings] = None):
        """
        Initialize the PDF converter.

        Args:
            settings: Configuration settings for the PDF converter
        """
        self.settings = settings or PDFConverterSettings()

        # Initialize components
        self.reader = PDFReader(self.settings.pdf_input_dir)
        self.parser = PDFParser(self.settings.field_mappings)
        self.converter = JSONConverter()
        self.writer = JSONLWriter(self.settings.json_output_dir)
        self.text_corrector = None  # Will be initialized if AI extraction is enabled

        logger.info(f"Initialized PDF converter with input directory: {self.settings.pdf_input_dir}")
        logger.info(f"Output directory: {self.settings.json_output_dir}")

        # Initialize text corrector if AI extraction is enabled
        if self.settings.use_ai_extraction:
            self.convert_with_ai(True)

    def convert_pdf(self, pdf_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Convert a single PDF file to JSON.

        Args:
            pdf_path: Path to the PDF file

        Returns:
            JSON data extracted from the PDF
        """
        pdf_path = Path(pdf_path) if isinstance(pdf_path, str) else pdf_path
        logger.info(f"Converting PDF file: {pdf_path}")

        # Read PDF
        pdf_content = self.reader.read_pdf(pdf_path)

        # Parse PDF content
        parsed_data = self.parser.parse_pdf_content(pdf_content)

        # Apply text correction if AI extraction is enabled
        if self.settings.use_ai_extraction and self.text_corrector and self.text_corrector.is_available():
            logger.info("Applying AI-enhanced text correction")
            # Fields that should be corrected (text fields)
            fields_to_correct = ["act", "description", "verdict", "citation"]
            parsed_data = self.text_corrector.correct_fields(parsed_data, fields_to_correct)

        # Convert to JSON
        json_data = self.converter.convert_to_json(parsed_data)

        return json_data

    def convert_pdf_to_jsonl(self, pdf_path: Union[str, Path], output_filename: Optional[str] = None) -> str:
        """
        Convert a single PDF file to JSONL and write to file.

        Args:
            pdf_path: Path to the PDF file
            output_filename: Name of the output file (without path)

        Returns:
            Path to the created JSONL file
        """
        pdf_path = Path(pdf_path) if isinstance(pdf_path, str) else pdf_path

        # Convert PDF to JSON
        json_data = self.convert_pdf(pdf_path)

        # Determine output filename if not provided
        if not output_filename:
            output_filename = f"{pdf_path.stem}.jsonl"

        # Write to JSONL file
        output_path = self.writer.write_jsonl([json_data], output_filename)

        return output_path

    def convert_directory(self, output_filename: str = "cases.jsonl", batch_size: Optional[int] = None) -> str:
        """
        Convert all PDF files in the input directory to a single JSONL file.

        This method catches any exceptions that occur during processing and logs them,
        then continues with the next file. It will not exit on errors. It also skips
        PDFs with empty or null content.

        Args:
            output_filename: Name of the output file (without path)
            batch_size: Number of PDFs to process in each batch (defaults to settings.batch_size)

        Returns:
            Path to the created JSONL file
        """
        batch_size = batch_size or self.settings.batch_size
        logger.info(f"Converting all PDFs in {self.settings.pdf_input_dir} to {output_filename}")

        # Get output path
        try:
            output_path = self.writer.get_output_path(output_filename)

            # Remove existing file if it exists
            if output_path.exists():
                logger.warning(f"Output file {output_path} already exists. It will be overwritten.")
                output_path.unlink()
        except Exception as e:
            logger.error(f"Error preparing output file {output_filename}: {str(e)}")
            # Create a default output path in case of error
            output_path = Path(self.settings.json_output_dir) / output_filename

        # Process PDFs in batches
        total_processed = 0

        try:
            # Iterate through batches of PDFs
            for batch in self.reader.read_pdfs_batch(batch_size):
                try:
                    # Parse each PDF in the batch
                    parsed_batch = []
                    for pdf_content in batch:
                        # Skip if pdf_content is empty or null
                        if not pdf_content or not pdf_content.get('content'):
                            logger.warning(f"Skipping PDF {pdf_content['metadata'].get('filename', 'unknown') if pdf_content else 'unknown'} due to empty content")
                            continue

                        try:
                            parsed_data = self.parser.parse_pdf_content(pdf_content)

                            # Apply text correction if AI extraction is enabled
                            if self.settings.use_ai_extraction and self.text_corrector and self.text_corrector.is_available():
                                try:
                                    # Fields that should be corrected (text fields)
                                    fields_to_correct = ["act", "description", "verdict"]
                                    parsed_data = self.text_corrector.correct_fields(parsed_data, fields_to_correct)
                                except Exception as e:
                                    logger.error(f"Error correcting text for PDF {pdf_content['metadata'].get('filename', 'unknown')}: {str(e)}")
                                    # Continue with uncorrected text

                            parsed_batch.append(parsed_data)
                        except Exception as e:
                            logger.error(f"Error parsing PDF {pdf_content['metadata'].get('filename', 'unknown')}: {str(e)}")
                            # Continue with next PDF

                    # Convert parsed data to JSON
                    try:
                        json_batch = self.converter.convert_batch_to_json(parsed_batch)
                    except Exception as e:
                        logger.error(f"Error converting batch to JSON: {str(e)}")
                        # Skip this batch if conversion fails
                        continue

                    # Append to JSONL file
                    try:
                        self.writer.append_jsonl(json_batch, output_filename)
                        total_processed += len(json_batch)
                        logger.info(f"Processed {total_processed} PDFs so far")
                    except Exception as e:
                        logger.error(f"Error writing batch to JSONL file: {str(e)}")
                        # Continue with next batch
                except Exception as e:
                    logger.error(f"Error processing batch: {str(e)}")
                    # Continue with next batch
        except Exception as e:
            logger.error(f"Error reading PDF batches: {str(e)}")
            # Continue to return the output path

        logger.info(f"Completed conversion of {total_processed} PDFs to {output_path}")
        return str(output_path)

    def convert_with_ai(self, use_ai: bool = True) -> None:
        """
        Set whether to use AI for enhanced text extraction.

        Args:
            use_ai: Whether to use AI for enhanced text extraction
        """
        self.settings.use_ai_extraction = use_ai
        logger.info(f"AI-enhanced extraction {'enabled' if use_ai else 'disabled'}")

        # Initialize or disable text corrector based on use_ai setting
        if use_ai:
            if self.text_corrector is None:
                logger.info("Initializing text corrector for AI-enhanced extraction")
                # Pass configuration options from settings
                self.text_corrector = TextCorrector(
                    model_name=self.settings.text_correction_model,
                    temperature=self.settings.text_correction_temperature
                )
                logger.info(f"Using model: {self.settings.text_correction_model} with temperature: {self.settings.text_correction_temperature}")
        else:
            self.text_corrector = None
            logger.info("Text corrector disabled")

    @classmethod
    def from_settings(cls, settings: PDFConverterSettings) -> 'PDFConverter':
        """
        Create a PDFConverter instance from settings.

        Args:
            settings: Configuration settings for the PDF converter

        Returns:
            PDFConverter instance
        """
        return cls(settings)
