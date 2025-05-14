"""
PDF Reader module.

This module provides a class for reading PDF files using PyMuPDF.
"""

import os
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Generator, Tuple
import pymupdf

logger = logging.getLogger(__name__)


class PDFReader:
    """Class for reading PDF files and extracting their content."""

    def __init__(self, input_dir: str):
        """
        Initialize the PDF reader.

        Args:
            input_dir: Directory containing PDF files to read
        """
        self.input_dir = Path(input_dir)
        if not self.input_dir.exists():
            logger.warning(f"Input directory {input_dir} does not exist. Creating it.")
            self.input_dir.mkdir(parents=True, exist_ok=True)

    def get_pdf_files(self) -> List[Path]:
        """
        Get a list of PDF files in the input directory.

        Returns:
            List of Path objects for PDF files
        """
        return [f for f in self.input_dir.glob("*.pdf") if f.is_file()]

    def read_pdf(self, pdf_path: Path) -> Dict[str, Any]:
        """
        Read a PDF file and extract its content.

        Args:
            pdf_path: Path to the PDF file

        Returns:
            Dictionary containing the PDF content with page numbers as keys
        """
        logger.info(f"Reading PDF file: {pdf_path}")

        try:
            # Open the PDF file
            doc = pymupdf.open(pdf_path)

            # Extract basic metadata
            metadata = {
                "filename": pdf_path.name,
                "path": str(pdf_path),
                "page_count": len(doc),
                "title": doc.metadata.get("title", ""),
                "author": doc.metadata.get("author", ""),
                "subject": doc.metadata.get("subject", ""),
                "keywords": doc.metadata.get("keywords", ""),
                "creator": doc.metadata.get("creator", ""),
                "producer": doc.metadata.get("producer", ""),
                "creation_date": doc.metadata.get("creationDate", ""),
                "modification_date": doc.metadata.get("modDate", ""),
            }

            # Extract text content from each page
            pages_content = {}
            for page_num, page in enumerate(doc):
                text = page.get_text()
                pages_content[f"page_{page_num+1}"] = text

            # Combine metadata and content
            result = {
                "metadata": metadata,
                "content": pages_content
            }

            return result

        except Exception as e:
            logger.error(f"Error reading PDF file {pdf_path}: {str(e)}")
            return {
                "metadata": {"filename": pdf_path.name, "path": str(pdf_path)},
                "content": {},
                "error": str(e)
            }

    def read_pdfs_batch(self, batch_size: int = 10) -> Generator[List[Dict[str, Any]], None, None]:
        """
        Read PDF files in batches.

        Args:
            batch_size: Number of PDFs to read in each batch

        Yields:
            List of dictionaries containing PDF content
        """
        pdf_files = self.get_pdf_files()

        for i in range(0, len(pdf_files), batch_size):
            batch = pdf_files[i:i+batch_size]
            results = []

            for pdf_file in batch:
                pdf_content = self.read_pdf(pdf_file)
                results.append(pdf_content)

            yield results
