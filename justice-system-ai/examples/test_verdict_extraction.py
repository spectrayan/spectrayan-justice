"""
Test script to directly extract the verdict field from a PDF file.

This script reads a PDF file, extracts its content, and then tries different
patterns to extract the verdict field. This helps us understand what's happening
and why our patterns aren't matching correctly.
"""

import os
import sys
import re
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils import PDFReader

def test_verdict_extraction():
    """Test different patterns for extracting the verdict field."""
    print("Testing verdict field extraction...")
    
    # Create a PDF reader
    reader = PDFReader("./data/pdfs")
    
    # Get the PDF files in the input directory
    pdf_files = reader.get_pdf_files()
    if not pdf_files:
        print("No PDF files found in ./data/pdfs")
        return
    
    # Read the first PDF file
    pdf_file = pdf_files[0]
    print(f"Reading PDF file: {pdf_file}")
    
    # Read the PDF content
    pdf_content = reader.read_pdf(pdf_file)
    
    # Combine all page content into a single string
    full_text = ""
    for page_key, page_text in pdf_content["content"].items():
        full_text += page_text + "\n"
    
    # Print the full text for inspection
    print("\nFull text (first 2000 characters):")
    print(full_text[:2000])
    
    # Try different patterns for extracting the verdict field
    print("\nTrying different patterns for extracting the verdict field:")
    
    # Pattern 1: Look for "Held, that" phrases
    print("\nPattern 1: Look for 'Held, that' phrases")
    held_patterns = [
        r"Held,\s+that\s+(.*?)(?=\n\n|\Z)",
        r"Held,?\s+that\s+(.*?)(?=\n\n|\Z)",
        r"Held[,.]?\s+[Tt]hat\s+(.*?)(?=\n\n|\Z)",
        r"[Hh]eld,?\s+that\s+(.*?)(?=\n\n|\Z)"
    ]
    
    for pattern in held_patterns:
        match = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
        if match:
            print(f"  Found match with pattern: {pattern}")
            print(f"  Content: {match.group(1)[:200]}...")
        else:
            print(f"  No match found with pattern: {pattern}")
    
    # Pattern 2: Look for HEADNOTE section and extract "Held" phrases from it
    print("\nPattern 2: Look for HEADNOTE section and extract 'Held' phrases from it")
    headnote_pattern = r"HEADNOTE\s*:\s*(.*?)(?=\n\s*[A-Z]+\s*:|\Z)"
    headnote_match = re.search(headnote_pattern, full_text, re.DOTALL | re.IGNORECASE)
    
    if headnote_match:
        print(f"  Found HEADNOTE section")
        headnote = headnote_match.group(1).strip()
        print(f"  HEADNOTE content: {headnote[:200]}...")
        
        # Look for "Held" phrases in the headnote
        held_match = re.search(r"Held,?\s+that\s+(.*?)(?=\n\n|\Z)", headnote, re.DOTALL | re.IGNORECASE)
        if held_match:
            print(f"  Found 'Held, that' phrase in HEADNOTE")
            print(f"  Content: {held_match.group(1)[:200]}...")
        else:
            print(f"  No 'Held, that' phrase found in HEADNOTE")
    else:
        print(f"  No HEADNOTE section found")
    
    # Pattern 3: Look for specific phrases in the full text
    print("\nPattern 3: Look for specific phrases in the full text")
    specific_phrases = [
        r"the appeal did not lie to the Supreme Court",
        r"it lay to the Appellate Bench of the High Court",
        r"The decrees of a single judge of the High Court"
    ]
    
    for phrase in specific_phrases:
        match = re.search(phrase, full_text, re.IGNORECASE)
        if match:
            print(f"  Found phrase: {phrase}")
            # Get more context around the match
            start = max(0, match.start() - 50)
            end = min(len(full_text), match.end() + 200)
            context = full_text[start:end].strip()
            print(f"  Context: {context}...")
        else:
            print(f"  Phrase not found: {phrase}")

if __name__ == "__main__":
    test_verdict_extraction()