"""
Example script demonstrating how to use the PDF to JSON converter.

This script shows how to convert PDF files to JSONL format using the PDFConverter class.
"""

import os
import sys
import logging
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config.settings import settings
from src.config.pdf_converter_config import PDFConverterSettings
from src.utils import PDFConverter


def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('pdf_converter.log')
        ]
    )


def convert_single_pdf():
    """Convert a single PDF file to JSONL."""
    # Get settings from the global settings
    pdf_settings = settings.pdf_converter

    # Create a converter instance
    converter = PDFConverter(pdf_settings)

    # Get the first PDF file in the input directory
    pdf_files = converter.reader.get_pdf_files()
    if not pdf_files:
        print(f"No PDF files found in {pdf_settings.pdf_input_dir}")
        return

    pdf_file = pdf_files[0]
    print(f"Converting single PDF file: {pdf_file}")

    # Convert the PDF to JSONL
    output_path = converter.convert_pdf_to_jsonl(pdf_file)
    print(f"Converted PDF to JSONL: {output_path}")

    # Also show the JSON data
    json_data = converter.convert_pdf(pdf_file)
    print("\nExtracted JSON data:")
    print(converter.converter.to_json_string(json_data, pretty=True))


def convert_directory():
    """Convert all PDF files in the input directory to a single JSONL file.

    This function demonstrates the use of the convert_directory method, which includes
    robust error handling that catches any exceptions during processing, logs them,
    and continues with the next file. It also automatically skips PDFs with empty or null
    content. This ensures that the conversion process doesn't stop if there are issues
    with individual files or if it encounters empty PDFs.
    """
    # Get settings from the global settings
    pdf_settings = settings.pdf_converter

    # Create a converter instance
    converter = PDFConverter(pdf_settings)

    # Count PDF files in the input directory
    pdf_files = converter.reader.get_pdf_files()
    if not pdf_files:
        print(f"No PDF files found in {pdf_settings.pdf_input_dir}")
        return

    print(f"Converting {len(pdf_files)} PDF files from {pdf_settings.pdf_input_dir}")

    # Convert all PDFs to a single JSONL file
    output_path = converter.convert_directory(output_filename="all_cases.jsonl")
    print(f"Converted all PDFs to JSONL: {output_path}")


def convert_with_custom_settings():
    """Convert PDF files using custom settings."""
    # Create custom settings
    custom_settings = PDFConverterSettings(
        pdf_input_dir="D:\\Spectrayan\\data\\archive\\pdfs",
        #pdf_input_dir="./data/pdfs",
        json_output_dir="./data/json",
        batch_size=5,
        use_ai_extraction=True
    )

    # Create a converter instance with custom settings
    converter = PDFConverter(custom_settings)

    # Ensure directories exist
    custom_settings.ensure_directories()

    print(f"Using custom input directory: {custom_settings.pdf_input_dir}")
    print(f"Using custom output directory: {custom_settings.json_output_dir}")

    # Count PDF files in the input directory
    pdf_files = converter.reader.get_pdf_files()
    if not pdf_files:
        print(f"No PDF files found in {custom_settings.pdf_input_dir}")
        print("Please copy some PDF files to this directory and run the example again.")
        return

    # Convert all PDFs to a single JSONL file
    # The convert_directory method includes robust error handling that catches any exceptions
    # during processing, logs them, and continues with the next file. It also automatically
    # skips PDFs with empty or null content.
    output_path = converter.convert_directory(output_filename="custom_cases.jsonl")
    print(f"Converted all PDFs to JSONL: {output_path}")


def main():
    """Run the example script."""
    setup_logging()

    print("PDF to JSON Converter Example")
    print("============================")

    # Check if data directories exist
    if not os.path.exists("./data/pdfs"):
        print("Creating data directories...")
        os.makedirs("./data/pdfs", exist_ok=True)
        os.makedirs("./data/json", exist_ok=True)
        os.makedirs("./data/custom_pdfs", exist_ok=True)
        os.makedirs("./data/custom_json", exist_ok=True)
        print("Please copy some PDF files to ./data/pdfs and run the example again.")
        return

    # Run examples
    #print("\n1. Converting a single PDF file")
    #print("------------------------------")
    #convert_single_pdf()

    #print("\nConverting all PDF files in a directory")
    #print("----------------------------------------")
    #convert_directory()

    print("\n3. Converting with custom settings")
    print("--------------------------------")
    convert_with_custom_settings()


if __name__ == "__main__":
    main()
