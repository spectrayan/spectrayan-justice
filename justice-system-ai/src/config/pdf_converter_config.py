"""
Configuration settings for PDF to JSON converter.

This module provides configuration settings for the PDF to JSON converter
using pydantic for validation.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from pathlib import Path


class PDFConverterSettings(BaseModel):
    """Configuration settings for the PDF to JSON converter."""

    # Input/Output directories
    pdf_input_dir: str = Field(
        default="./data/pdfs",
        description="Directory containing PDF files to convert"
    )
    json_output_dir: str = Field(
        default="./data/json",
        description="Directory where JSON files will be saved"
    )

    # Processing settings
    batch_size: int = Field(
        default=10,
        description="Number of PDFs to process in a batch"
    )
    use_ai_extraction: bool = Field(
        default=True,
        description="Whether to use AI for enhanced text extraction"
    )

    # Text correction settings
    text_correction_model: str = Field(
        default="llama3.2:latest",
        description="Name of the Ollama model to use for text correction"
    )
    text_correction_temperature: float = Field(
        default=0.1,
        description="Temperature parameter for text generation (lower values are more deterministic)"
    )

    # Field mapping settings
    field_mappings: Dict[str, List[str]] = Field(
        default={
            "act": ["Act"],
            "description": ["Headnote"],
            "verdict": ["Judgment"],
            "judgementDate": ["Date of Judgment", "Judgment Date", "Date"]
        },
        description="Mapping of output fields to possible PDF section titles"
    )

    def get_input_path(self) -> Path:
        """Return the input directory as a Path object."""
        return Path(self.pdf_input_dir)

    def get_output_path(self) -> Path:
        """Return the output directory as a Path object."""
        return Path(self.json_output_dir)

    def ensure_directories(self) -> None:
        """Ensure input and output directories exist."""
        self.get_input_path().mkdir(parents=True, exist_ok=True)
        self.get_output_path().mkdir(parents=True, exist_ok=True)
