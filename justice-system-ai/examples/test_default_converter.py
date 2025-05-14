"""
Test script to directly use the PDFConverter with the default settings.

This script creates a PDFConverter with the default settings, converts a PDF file,
and prints the extracted fields to verify that the field mappings update is working.
"""

import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils import PDFConverter

def test_default_converter():
    """Test the PDFConverter with default settings."""
    print("Testing PDFConverter with default settings...")
    
    # Create a converter with default settings
    converter = PDFConverter()
    
    # Get the PDF files in the input directory
    pdf_files = converter.reader.get_pdf_files()
    if not pdf_files:
        print(f"No PDF files found in {converter.settings.pdf_input_dir}")
        return
    
    # Convert the first PDF file
    pdf_file = pdf_files[0]
    print(f"Converting PDF file: {pdf_file}")
    
    # Convert the PDF to JSON
    json_data = converter.convert_pdf(pdf_file)
    
    # Print the extracted fields
    print("\nExtracted fields:")
    print(f"ID: {json_data.get('id', '')}")
    print(f"Citation: {json_data.get('citation', '')}")
    print(f"Act: {json_data.get('act', '')}")
    print(f"Description: {json_data.get('description', '')}")
    print(f"Verdict: {json_data.get('verdict', '')}")
    print(f"Judgment Date: {json_data.get('judgementDate', '')}")
    
    # Check for newline characters in string fields
    for field in ["act", "description", "verdict", "citation"]:
        if json_data.get(field) and '\n' in json_data[field]:
            print(f"\nWARNING: Newline characters found in {field} field!")
        else:
            print(f"\n{field} field has no newline characters - Good!")
    
    # Convert the PDF to JSONL
    output_path = converter.convert_pdf_to_jsonl(pdf_file, "test_default.jsonl")
    print(f"\nConverted PDF to JSONL: {output_path}")
    
    # Read the JSONL file and print its contents
    with open(output_path, 'r', encoding='utf-8') as f:
        jsonl_content = f.read()
    
    print("\nJSONL content:")
    print(jsonl_content)

if __name__ == "__main__":
    test_default_converter()