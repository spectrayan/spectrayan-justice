"""
Logging configuration for Spectrayan Model.

This module sets up logging for the application using loguru.
"""

import sys
from pathlib import Path

from loguru import logger

from config.settings import settings


def setup_logging():
    """
    Configure logging for the application.
    
    This function sets up logging with loguru, configuring log level and output destinations
    based on the application settings.
    """
    # Remove default logger
    logger.remove()
    
    # Add console logger
    logger.add(
        sys.stderr,
        level=settings.log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    )
    
    # Add file logger
    log_file = Path(settings.log_file)
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    logger.add(
        log_file,
        level=settings.log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="10 MB",
        retention="1 month",
    )
    
    logger.info(f"Logging initialized with level: {settings.log_level}")
    logger.info(f"Log file: {settings.log_file}")
    
    return logger


# Initialize logger
logger = setup_logging()