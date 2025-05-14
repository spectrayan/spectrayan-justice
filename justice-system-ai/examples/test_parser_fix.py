"""
Test script to verify the fix for the PDF parser issue.

This script converts a sample PDF file and prints the extracted fields to verify
that the verdict field correctly extracts judgment text (not date) and that
newline characters are replaced with spaces in string fields.
"""

import os
import sys
import json
import re
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config.settings import settings
from src.utils import PDFConverter

def test_parser_fix():
    """Test the fix for the PDF parser issue."""
    print("Testing PDF parser fix...")

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

    # Read the PDF content first to examine it
    pdf_content = converter.reader.read_pdf(pdf_file)

    # Combine all page content into a single string
    full_text = ""
    for page_key, page_text in pdf_content["content"].items():
        full_text += page_text + "\n"

    # Print sections of interest
    print("\nSearching for JUDGMENT and DATE OF JUDGMENT sections in the PDF:")

    # Look for JUDGMENT sections
    judgment_patterns = [
        r"JUDGMENT\s*:\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)",
        r"JUDGMENT\s*\n\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)",
        r"JUDGEMENT\s*:\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)",
        r"JUDGEMENT\s*\n\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)"
    ]

    for pattern in judgment_patterns:
        matches = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
        if matches:
            print(f"\nFound JUDGMENT section with pattern: {pattern}")
            print(f"Content: {matches.group(1)[:100]}...")

    # Look for DATE OF JUDGMENT sections
    date_patterns = [
        r"DATE\s+OF\s+JUDGMENT\s*:\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)",
        r"DATE\s+OF\s+JUDGMENT\s*\n\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)",
        r"JUDGMENT\s+DATE\s*:\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)",
        r"JUDGMENT\s+DATE\s*\n\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)"
    ]

    for pattern in date_patterns:
        matches = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
        if matches:
            print(f"\nFound DATE OF JUDGMENT section with pattern: {pattern}")
            print(f"Content: {matches.group(1)[:100]}...")

    # Look for "Held, that" phrases
    held_patterns = [
        r"Held,\s+that\s+(.*?)(?=\n\n|\Z)",
        r"The\s+[Cc]ourt\s+held\s+that\s+(.*?)(?=\n\n|\Z)"
    ]

    for pattern in held_patterns:
        matches = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
        if matches:
            print(f"\nFound 'Held, that' phrase with pattern: {pattern}")
            print(f"Content: {matches.group(1)[:200]}...")

    # Print the full text for inspection
    print("\nFull text (first 1000 characters):")
    print(full_text[:1000])

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
    output_path = converter.convert_pdf_to_jsonl(pdf_file, "test_fix.jsonl")
    print(f"\nConverted PDF to JSONL: {output_path}")

    # Read the JSONL file and print its contents
    with open(output_path, 'r', encoding='utf-8') as f:
        jsonl_content = f.read()

    print("\nJSONL content:")
    print(jsonl_content)

    # Convert all PDFs in the directory
    print("\nConverting all PDFs in the directory...")
    output_path = converter.convert_directory(output_filename="all_cases_fixed.jsonl")
    print(f"Converted all PDFs to JSONL: {output_path}")

    # Read the JSONL file and print its contents
    with open(output_path, 'r', encoding='utf-8') as f:
        jsonl_content = f.readlines()

    print("\nAll cases JSONL content (first line):")
    if jsonl_content:
        print(jsonl_content[0].strip())

if __name__ == "__main__":
    test_parser_fix()
