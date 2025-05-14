"""
PDF Parser module.

This module provides a class for parsing PDF content and extracting structured information.
"""

import re
import logging
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime

logger = logging.getLogger(__name__)


class PDFParser:
    """Class for parsing PDF content and extracting structured information."""

    def __init__(self, field_mappings: Dict[str, List[str]]):
        """
        Initialize the PDF parser.

        Args:
            field_mappings: Mapping of output fields to possible PDF section titles
        """
        self.field_mappings = field_mappings

    def _remove_headers(self, page_text: str) -> str:
        """
        Remove common headers from page text.

        Args:
            page_text: Text content of a page

        Returns:
            Text content with headers removed
        """
        if not page_text:
            return page_text

        # Define patterns for common headers
        court_patterns = [
            r"SUPREME COURT OF INDIA",
            r"HIGH COURT OF \w+",  # HIGH COURT OF [STATE]
        ]

        page_pattern = r"Page\s+\d+\s+of\s+\d+"  # Page X of Y

        # Other patterns that can be removed independently
        other_patterns = [
            r"http://JUDIS\.NIC\.IN",
            r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/\S*)?",  # Any URL in headers
            r"^\s*\d+\s*$",  # Standalone page numbers
            r"^\s*-\s*\d+\s*-\s*$",  # Page numbers like - 1 -
            r"^\s*\[\s*\d+\s*\]\s*$",  # Page numbers like [ 1 ]
            r"^Printed For.*$",  # Printed For... lines
            r"^Printed from.*$",  # Printed from... lines
            r"^Courtesy:.*$",  # Courtesy: lines
            r"^Copyright:.*$",  # Copyright: lines
        ]


        # Process the text line by line to better handle headers at top and bottom of pages
        lines = page_text.split("\n")
        cleaned_lines = []

        # Skip first few lines if they match header patterns (top headers)
        start_idx = 0
        max_header_lines = min(5, len(lines))  # Check up to first 5 lines

        # Concatenate the first 5 lines to handle headers split across multiple lines
        first_lines_concat = " ".join([lines[i] for i in range(max_header_lines)])
        #logger.info(f"Concatenated first {max_header_lines} lines: {first_lines_concat}")

        # Check if concatenated text contains Page X of Y pattern
        has_page_pattern = re.search(page_pattern, first_lines_concat, re.IGNORECASE) is not None

        # For court patterns, only match if Page X of Y is in the concatenated text
        court_match = False
        if has_page_pattern:
            #logger.info(f"Page pattern found in concatenated text: {first_lines_concat}")
            court_match = any(re.search(pattern, first_lines_concat, re.IGNORECASE) for pattern in court_patterns)

        # For individual lines, check other patterns independently
        for i in range(max_header_lines):
            line = lines[i]
            #logger.info(f"cleaning at Line {i}: {line}")

            # For other patterns, match independently
            other_match = any(re.search(pattern, line, re.IGNORECASE) for pattern in other_patterns)

            if court_match or other_match:
                start_idx = i + 1
            else:
                # Stop if we find a non-header line
                break

        # Skip last few lines if they match header patterns (bottom headers/footers)
        end_idx = len(lines)
        last_lines_start = max(len(lines) - 5, start_idx)

        # Concatenate the last 5 lines to handle footers split across multiple lines
        last_lines = lines[last_lines_start:len(lines)]
        last_lines_concat = " ".join(last_lines)
        #logger.info(f"Concatenated last {len(last_lines)} lines: {last_lines_concat}")

        # Check if concatenated text contains Page X of Y pattern
        has_page_pattern = re.search(page_pattern, last_lines_concat, re.IGNORECASE) is not None

        # For court patterns, only match if Page X of Y is in the concatenated text
        court_match = False
        if has_page_pattern:
            #logger.info(f"Page pattern found in concatenated footer text: {last_lines_concat}")
            court_match = any(re.search(pattern, last_lines_concat, re.IGNORECASE) for pattern in court_patterns)

        # For individual lines, check other patterns independently
        for i in range(len(lines) - 1, last_lines_start, -1):
            line = lines[i]

            # For other patterns, match independently
            other_match = any(re.search(pattern, line, re.IGNORECASE) for pattern in other_patterns)

            if court_match or other_match:
                end_idx = i
            else:
                # Stop if we find a non-header line
                break

        # Process remaining lines
        i = start_idx
        while i < end_idx:
            # Check for potential headers in chunks of up to 3 lines
            chunk_end = min(i + 3, end_idx)
            chunk_lines = lines[i:chunk_end]
            chunk_text = " ".join(chunk_lines)

            # Check if chunk contains Page X of Y pattern
            has_page_pattern = re.search(page_pattern, chunk_text, re.IGNORECASE) is not None

            # For court patterns, only match if Page X of Y is in the chunk
            court_match = False
            if has_page_pattern:
                court_match = any(re.search(pattern, chunk_text, re.IGNORECASE) for pattern in court_patterns)

                if court_match:
                    # Skip all lines in this chunk
                    i = chunk_end
                    continue

            # Process individual lines for other patterns
            line = lines[i]

            # For other patterns, match independently
            other_match = any(re.search(pattern, line, re.IGNORECASE) for pattern in other_patterns)

            # Skip if other patterns match
            if other_match:
                i += 1
                continue

            # Skip very short lines (likely page numbers or other artifacts)
            if len(line.strip()) <= 3:
                i += 1
                continue

            cleaned_lines.append(line)
            i += 1

        return "\n".join(cleaned_lines)

    def parse_pdf_content(self, pdf_content: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse PDF content and extract structured information.

        Args:
            pdf_content: Dictionary containing PDF content from PDFReader

        Returns:
            Dictionary containing structured information extracted from the PDF
        """
        logger.info(f"Parsing PDF content: {pdf_content['metadata']['filename']}")

        # Initialize result with basic metadata
        result = {
            "source_file": pdf_content["metadata"]["filename"],
            "id": "",
            "act": "",
            "description": "",
            "verdict": "",
            "judgementDate": ""
        }

        # Combine all page content into a single string for easier processing
        full_text = ""
        for page_key, page_text in pdf_content["content"].items():
            # Remove headers before adding to full text
            cleaned_page_text = self._remove_headers(page_text)
            full_text += cleaned_page_text + "\n"

        # Extract each required field
        for field, possible_headers in self.field_mappings.items():
            value = self._extract_field(full_text, possible_headers)
            if value:
                result[field] = value

        # Special handling for judgementDate - try to parse as date
        if result["judgementDate"]:
            result["judgementDate"] = self._parse_date(result["judgementDate"])


        # Generate ID if not found
        if not result["id"]:
            result["id"] = self._generate_id(pdf_content["metadata"]["filename"], result)

        # Replace newline characters with spaces in string fields
        for field in ["act", "description", "verdict"]:
            if result[field]:
                result[field] = re.sub(r'\n+', ' ', result[field])

        return result

    def _looks_like_date(self, text: str) -> bool:
        """
        Check if a string looks like a date.

        Args:
            text: String to check

        Returns:
            True if the string looks like a date, False otherwise
        """
        # Check if the string is short (like a date)
        if len(text) > 15:
            return False

        # Check if the string matches common date patterns
        date_patterns = [
            r"^\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}$",  # DD/MM/YYYY or DD-MM-YYYY
            r"^\d{4}[/.-]\d{1,2}[/.-]\d{1,2}$",  # YYYY/MM/DD or YYYY-MM-DD
            r"^\d{1,2}\s+[A-Za-z]+\s+\d{4}$",  # DD Month YYYY
            r"^[A-Za-z]+\s+\d{1,2},?\s+\d{4}$"  # Month DD, YYYY
        ]

        for pattern in date_patterns:
            if re.match(pattern, text, re.IGNORECASE):
                return True

        return False

    def _extract_field(self, text: str, possible_headers: List[str]) -> str:
        """
        Extract a field from text based on possible headers.

        Args:
            text: Full text content
            possible_headers: List of possible headers for the field

        Returns:
            Extracted field value or empty string if not found
        """
        # Define all possible section headers that can appear in the PDF
        section_headers = [
            "CASE NO", "PETITIONER", "RESPONDENT", "DATE OF JUDGMENT",
            "BENCH", "ACT", "HEADNOTE", "JUDGMENT:"
        ]

        # Create a regex pattern that matches any of the section headers
        section_pattern = "|".join([rf"{re.escape(header)}\s*:" for header in section_headers])
        section_pattern_caps = "|".join([rf"{re.escape(header.upper())}" for header in section_headers])

        for header in possible_headers:
            # Try different patterns for finding the field
            logger.debug(f"Trying to extract field '{header}'...")
            patterns = [
                # Pattern 1: Header followed by colon and content until next section
                rf"{re.escape(header)}\s*:\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                # Pattern 2: Header as a standalone line followed by content until next section
                rf"{re.escape(header)}\s*\n\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                # Pattern 3: Header in all caps followed by content until next section
                rf"{re.escape(header.upper())}\s*\n\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
            ]
            if header == "Judgment":
                patterns = [
                    # Pattern 1: Header followed by colon and content until next section
                    rf"(?<!Date Of\s){re.escape(header)}\s*:\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                    # Pattern 2: Header as a standalone line followed by content until next section
                    rf"(?<!Date Of\s){re.escape(header)}\s*\n\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                    # Pattern 3: Header in all caps followed by content until next section
                    rf"(?<!Date Of\s){re.escape(header.upper())}\s*\n\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                ]


            for pattern in patterns:
                matches = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
                if matches:
                    logger.debug(f"Pattern '{pattern}' matched. Extracting value...")
                    value = matches.group(1).strip()
                    logger.debug(f"Pattern '{pattern}' matched. Extracted value: {value}")
                    return value

        # If no match found with headers, try content-based extraction
        return self._extract_by_content(text, possible_headers)

    def _extract_by_content(self, text: str, possible_headers: List[str]) -> str:
        """
        Extract field based on content patterns when headers are not found.

        Args:
            text: Full text content
            possible_headers: List of possible headers for the field (used for context)

        Returns:
            Extracted field value or empty string if not found
        """
        # Define section headers for delimiting content
        section_headers = [
            "CASE NO", "PETITIONER", "RESPONDENT", "DATE OF JUDGMENT",
            "BENCH", "ACT", "HEADNOTE", "JUDGMENT", "JUDGEMENT"
        ]
        field_type = next(iter(k for k, v in self.field_mappings.items() if v == possible_headers), "")

        if field_type == "act":

            section_pattern = "|".join([rf"{re.escape(header)}\s*:" for header in section_headers])
            section_pattern_caps = "|".join([rf"{re.escape(header.upper())}" for header in section_headers])

            # First try to find the ACT section and extract all content until the next section
            act_section_patterns = [
                rf"ACT\s*:\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                rf"ACT\s*\n\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)"
            ]

            for pattern in act_section_patterns:
                match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
                if match:
                    return match.group(1).strip()

            # If no ACT section found, look for act patterns
            act_patterns = [
                r"([A-Z][a-z]+\s+Act,?\s+\d{4})",
                r"([A-Z][a-z]+\s+[A-Z][a-z]+\s+Act,?\s+\d{4})",
                r"(Act\s+No\.\s+\d+\s+of\s+\d{4})"
            ]
            for pattern in act_patterns:
                matches = re.findall(pattern, text)
                if matches:
                    return ", ".join(set(matches))

        elif field_type == "description":

            section_pattern = "|".join([rf"{re.escape(header)}\s*:" for header in section_headers])
            section_pattern_caps = "|".join([rf"{re.escape(header.upper())}" for header in section_headers])

            # Look for headnote sections
            headnote_patterns = [
                rf"HEADNOTE\s*:\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                rf"HEADNOTE\s*\n\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                rf"SUMMARY\s*:\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                rf"SYNOPSIS\s*:\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)"
            ]

            for pattern in headnote_patterns:
                match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
                if match:
                    return match.group(1).strip()

            return ""

        elif field_type == "verdict":


            section_pattern = "|".join([rf"{re.escape(header)}\s*:" for header in section_headers])
            section_pattern_caps = "|".join([rf"{re.escape(header.upper())}" for header in section_headers])

            # As a last resort, check if there's a JUDGMENT section that contains more than just a date
            judgment_section_patterns = [
                rf"JUDGMENT\s*:\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                rf"JUDGMENT\s*\n\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                rf"JUDGEMENT\s*:\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)",
                rf"JUDGEMENT\s*\n\s*(.*?)(?=\n\s*(?:{section_pattern}|{section_pattern_caps})|\Z)"
            ]

            for pattern in judgment_section_patterns:
                match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
                if match:
                    content = match.group(1).strip()
                    # Check if the content is more than just a date
                    if len(content) > 15 and not re.match(r'^\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}$', content):
                        return content

        return ""

    def _parse_date(self, date_str: str) -> str:
        """
        Parse date string into a standardized format.

        Args:
            date_str: Date string to parse

        Returns:
            Standardized date string (YYYY-MM-DD) or original string if parsing fails
        """
        date_patterns = [
            r"(\d{1,2})(?:st|nd|rd|th)?\s+(?:of\s+)?([A-Za-z]+),?\s+(\d{4})",  # 15th August, 2023
            r"(\d{1,2})[./](\d{1,2})[./](\d{4})",  # 15/08/2023 or 15.08.2023
            r"(\d{4})[./](\d{1,2})[./](\d{1,2})",  # 2023/08/15 or 2023.08.15
            r"([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})"  # August 15, 2023
        ]

        month_map = {
            "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
            "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
            "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7, "aug": 8, 
            "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12
        }

        for pattern in date_patterns:
            match = re.search(pattern, date_str, re.IGNORECASE)
            if match:
                groups = match.groups()

                if len(groups) == 3:
                    # Check pattern type
                    if re.match(r"\d{1,2}[./]\d{1,2}[./]\d{4}", match.group(0)):
                        # DD/MM/YYYY format
                        day, month, year = groups
                        try:
                            return f"{year}-{int(month):02d}-{int(day):02d}"
                        except ValueError:
                            pass
                    elif re.match(r"\d{4}[./]\d{1,2}[./]\d{1,2}", match.group(0)):
                        # YYYY/MM/DD format
                        year, month, day = groups
                        try:
                            return f"{year}-{int(month):02d}-{int(day):02d}"
                        except ValueError:
                            pass
                    else:
                        # Text month format
                        if match.group(0)[0].isdigit():
                            day, month_str, year = groups
                        else:
                            month_str, day, year = groups

                        month_str = month_str.lower()
                        if month_str in month_map:
                            month_num = month_map[month_str]
                            try:
                                return f"{year}-{month_num:02d}-{int(day):02d}"
                            except ValueError:
                                pass

        # If no pattern matches, return the original string
        return date_str

    def _generate_id(self, filename: str, parsed_data: Dict[str, Any]) -> str:
        """
        Generate an ID for the document if one wasn't found.

        Args:
            filename: Name of the source file
            parsed_data: Already parsed data that might contain useful information

        Returns:
            Generated ID
        """

        # Use filename without extension as fallback
        clean_filename = re.sub(r'[^\w\d]', '_', filename)
        if clean_filename.lower().endswith('.pdf'):
            clean_filename = clean_filename[:-4]

        return f"case_{clean_filename}"
