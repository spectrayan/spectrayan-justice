"""
Example script demonstrating the text correction functionality.

This script shows how to use the text correction feature to correct spelling and grammar
in extracted text from PDF files before writing to JSON.
"""

import logging
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config.pdf_converter_config import PDFConverterSettings
from src.utils.pdf2json.pdf_converter import PDFConverter
from src.utils.pdf2json.text_corrector import TextCorrector

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('examples/logs/text_correction_example.log')
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Run the text correction example."""
    # Create output directories if they don't exist
    Path('examples/logs').mkdir(parents=True, exist_ok=True)
    
    # Example 1: Direct use of TextCorrector
    logger.info("Example 1: Direct use of TextCorrector")
    
    # Create a TextCorrector instance
    corrector = TextCorrector(model_name="llama2", temperature=0.1)
    
    # Example text with spelling and grammar errors
    text_with_errors = """
    The judgement was deliverd on 5th Aprile, 2023. The court rejcted the 
    petitioners arguements and upheld the validity of the impugned provisions. 
    The court observd that the legislature has wide discretion in matters of 
    economic policy and the court should not interfere unless the policy is 
    manifestly arbitrary or unreasonable.
    """
    
    # Correct the text
    if corrector.is_available():
        corrected_text = corrector.correct_text(text_with_errors)
        logger.info(f"Original text: {text_with_errors}")
        logger.info(f"Corrected text: {corrected_text}")
    else:
        logger.warning("TextCorrector is not available. Make sure Ollama is running.")
    
    # Example 2: Using PDFConverter with AI-enhanced text correction
    logger.info("\nExample 2: Using PDFConverter with AI-enhanced text correction")
    
    # Create custom settings
    settings = PDFConverterSettings(
        pdf_input_dir="examples/data/pdfs",
        json_output_dir="examples/data/json",
        use_ai_extraction=True,  # Enable AI-enhanced text extraction
        text_correction_model="llama2",
        text_correction_temperature=0.1
    )
    
    # Create a PDFConverter instance with the custom settings
    converter = PDFConverter(settings)
    
    # List available PDF files
    pdf_dir = Path(settings.pdf_input_dir)
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    if pdf_files:
        # Convert the first PDF file with text correction
        pdf_path = pdf_files[0]
        logger.info(f"Converting PDF file: {pdf_path}")
        
        # Convert the PDF to JSON with text correction
        output_path = converter.convert_pdf_to_jsonl(pdf_path)
        logger.info(f"PDF converted to JSONL: {output_path}")
    else:
        logger.warning(f"No PDF files found in {pdf_dir}")
        logger.info("You can place PDF files in the examples/data/pdfs directory to test the conversion.")


if __name__ == "__main__":
    main()