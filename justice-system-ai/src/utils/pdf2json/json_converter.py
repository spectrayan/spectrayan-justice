"""
JSON Converter module.

This module provides a class for converting parsed PDF data into standardized JSON format.
"""

import logging
import json
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)


class JSONConverter:
    """Class for converting parsed PDF data into standardized JSON format."""

    def __init__(self):
        """Initialize the JSON converter."""
        pass
        
    def convert_to_json(self, parsed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert parsed PDF data into standardized JSON format.

        Args:
            parsed_data: Dictionary containing parsed PDF data

        Returns:
            Dictionary in standardized JSON format
        """
        logger.info(f"Converting parsed data to JSON: {parsed_data.get('source_file', 'unknown')}")
        
        # Create standardized JSON structure
        json_data = {
            "id": parsed_data.get("id", ""),
            "act": parsed_data.get("act", ""),
            "description": parsed_data.get("description", ""),
            "verdict": parsed_data.get("verdict", ""),
            "judgementDate": parsed_data.get("judgementDate", "")
        }
        
        # Add source file information
        if "source_file" in parsed_data:
            json_data["source_file"] = parsed_data["source_file"]
            
        # Validate required fields
        self._validate_json(json_data)
        
        return json_data
    
    def convert_batch_to_json(self, parsed_data_batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Convert a batch of parsed PDF data into standardized JSON format.

        Args:
            parsed_data_batch: List of dictionaries containing parsed PDF data

        Returns:
            List of dictionaries in standardized JSON format
        """
        return [self.convert_to_json(item) for item in parsed_data_batch]
    
    def _validate_json(self, json_data: Dict[str, Any]) -> None:
        """
        Validate JSON data and log warnings for missing required fields.

        Args:
            json_data: Dictionary containing JSON data
        """
        required_fields = ["id", "act", "description", "verdict", "judgementDate"]
        
        for field in required_fields:
            if not json_data.get(field):
                logger.warning(f"Missing or empty required field '{field}' in document {json_data.get('id', 'unknown')}")
                
    def to_json_string(self, json_data: Dict[str, Any], pretty: bool = False) -> str:
        """
        Convert JSON data to a JSON string.

        Args:
            json_data: Dictionary containing JSON data
            pretty: Whether to format the JSON string with indentation

        Returns:
            JSON string
        """
        if pretty:
            return json.dumps(json_data, indent=2, ensure_ascii=False)
        else:
            return json.dumps(json_data, ensure_ascii=False)