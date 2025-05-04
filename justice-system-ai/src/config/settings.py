"""
Configuration settings for Spectrayan Model.

This module loads environment variables and provides configuration settings
for the rest of the application using pydantic for validation and hierarchical
structure with separate settings for voice and vision.
"""

import os
from pathlib import Path
from typing import Any, Dict, Optional, List
from functools import lru_cache

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for the application using pydantic BaseSettings."""

    # Common settings

    # Logging
    log_level: str = Field(default="INFO")
    log_file: str = Field(default="./logs/spectrayan.log")


    def __init__(self, **kwargs):
        """Initialize settings and ensure directories exist."""
        super().__init__(**kwargs)

        # Ensure log directory exists
        log_dir = os.path.dirname(self.log_file)
        Path(log_dir).mkdir(parents=True, exist_ok=True)


    def as_dict(self) -> Dict[str, Any]:
        """Return settings as a dictionary."""
        result = {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_") and not callable(value)
        }
        return result


# Create a singleton instance
@lru_cache
def get_settings() -> Settings:
    """Get the settings instance (singleton)."""
    return Settings()


settings = get_settings()
