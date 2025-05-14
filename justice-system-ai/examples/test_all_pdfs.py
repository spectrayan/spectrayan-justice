"""
Test script to convert all PDFs in the directory and verify the fixes.

This script converts all PDFs in the directory and prints the extracted fields
to verify that the verdict field is correctly extracted and newline characters
are replaced with spaces in all string fields.
"""

import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils import PDFConverter

def test_all_pdfs():
    """Test the PDFConverter on all PDFs in the directory."""
    print("Testing PDFConverter on all PDFs in the directory...")
    
    # Create a converter with default settings
    converter = PDFConverter()
    
    # Get the PDF files in the input directory
    pdf_files = converter.reader.get_pdf_files()
    if not pdf_files:
        print(f"No PDF files found in {converter.settings.pdf_input_dir}")
        return
    
    print(f"Found {len(pdf_files)} PDF files in {converter.settings.pdf_input_dir}")
    
    # Convert all PDFs in the directory
    output_path = converter.convert_directory(output_filename="all_cases_fixed.jsonl")
    print(f"Converted all PDFs to JSONL: {output_path}")
    
    # Read the JSONL file and check each record
    with open(output_path, 'r', encoding='utf-8') as f:
        jsonl_content = f.readlines()
    
    print(f"\nChecking {len(jsonl_content)} records in the JSONL file...")
    
    for i, line in enumerate(jsonl_content):
        import json
        record = json.loads(line)
        
        print(f"\nRecord {i+1}:")
        print(f"Source file: {record.get('source_file', '')}")
        
        # Check if verdict field contains a date
        verdict = record.get('verdict', '')
        if verdict and len(verdict) <= 15 and any(c.isdigit() for c in verdict):
            print(f"WARNING: Verdict field might contain a date: {verdict}")
        else:
            print(f"Verdict field looks good: {verdict[:100]}...")
        
        # Check for newline characters in string fields
        for field in ["act", "description", "verdict", "citation"]:
            if record.get(field) and '\n' in record[field]:
                print(f"WARNING: Newline characters found in {field} field!")
            else:
                print(f"{field} field has no newline characters - Good!")

if __name__ == "__main__":
    test_all_pdfs()