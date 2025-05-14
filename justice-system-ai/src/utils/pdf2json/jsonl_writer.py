"""
JSONL Writer module.

This module provides a class for writing JSON data to JSONL files.
"""

import os
import logging
import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Union

logger = logging.getLogger(__name__)


class JSONLWriter:
    """Class for writing JSON data to JSONL files."""

    def __init__(self, output_dir: str):
        """
        Initialize the JSONL writer.

        Args:
            output_dir: Directory where JSONL files will be saved
        """
        self.output_dir = Path(output_dir)
        if not self.output_dir.exists():
            logger.warning(f"Output directory {output_dir} does not exist. Creating it.")
            self.output_dir.mkdir(parents=True, exist_ok=True)
            
    def write_jsonl(self, json_data: List[Dict[str, Any]], filename: str) -> str:
        """
        Write JSON data to a JSONL file.

        Args:
            json_data: List of dictionaries to write to the file
            filename: Name of the output file (without path)

        Returns:
            Path to the created JSONL file
        """
        # Ensure filename has .jsonl extension
        if not filename.lower().endswith('.jsonl'):
            filename += '.jsonl'
            
        output_path = self.output_dir / filename
        logger.info(f"Writing {len(json_data)} records to JSONL file: {output_path}")
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                for item in json_data:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
                    
            logger.info(f"Successfully wrote {len(json_data)} records to {output_path}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"Error writing to JSONL file {output_path}: {str(e)}")
            raise
            
    def append_jsonl(self, json_data: Union[Dict[str, Any], List[Dict[str, Any]]], filename: str) -> str:
        """
        Append JSON data to an existing JSONL file or create a new one.

        Args:
            json_data: Dictionary or list of dictionaries to append to the file
            filename: Name of the output file (without path)

        Returns:
            Path to the JSONL file
        """
        # Ensure filename has .jsonl extension
        if not filename.lower().endswith('.jsonl'):
            filename += '.jsonl'
            
        output_path = self.output_dir / filename
        
        # Convert single item to list for consistent processing
        if not isinstance(json_data, list):
            json_data = [json_data]
            
        logger.info(f"Appending {len(json_data)} records to JSONL file: {output_path}")
        
        try:
            with open(output_path, 'a', encoding='utf-8') as f:
                for item in json_data:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
                    
            logger.info(f"Successfully appended {len(json_data)} records to {output_path}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"Error appending to JSONL file {output_path}: {str(e)}")
            raise
            
    def get_output_path(self, filename: str) -> Path:
        """
        Get the full path for an output file.

        Args:
            filename: Name of the output file (without path)

        Returns:
            Path object for the output file
        """
        # Ensure filename has .jsonl extension
        if not filename.lower().endswith('.jsonl'):
            filename += '.jsonl'
            
        return self.output_dir / filename