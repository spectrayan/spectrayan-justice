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

    # Example text with spelling and grammar errors (small sample)
    text_with_errors_small = """
    The judgement was deliverd on 5th Aprile, 2023. The court rejcted the 
    petitioners arguements and upheld the validity of the impugned provisions. 
    The court observd that the legislature has wide discretion in matters of 
    economic policy and the court should not interfere unless the policy is 
    manifestly arbitrary or unreasonable.
    """

    # Example text with spelling and grammar errors (large sample to test chunking)
    text_with_errors_large = """
    The judgement was deliverd on 5th Aprile, 2023. The court rejcted the 
    petitioners arguements and upheld the validity of the impugned provisions. 
    The court observd that the legislature has wide discretion in matters of 
    economic policy and the court should not interfere unless the policy is 
    manifestly arbitrary or unreasonable. The petitioner, Mr. John Smith, had 
    filed the petition challenging Section 66A of the Information Technology Act.

    The respondant, represented by Ms. Jane Doe, argued that the provision was 
    necessary to prevent misuse of social media platforms. The court noted that 
    while the objective of the provision was legitimate, the language used was 
    vague and ambigous. The court held that the provision was unconstitutional 
    as it violated Article 19(1)(a) of the Constitution.

    The court also observd that the provision was not saved by Article 19(2) as 
    it did not fall within any of the permissible restrictions. The court directed 
    the government to revise the provision in accordance with the constitutional 
    principles. The court also awarded costs of Rs. 50,000 to the petitioner.

    The judgement has far-reaching implications for freedom of speech and expression 
    in the digital age. It reaffirms the principle that restrictions on fundamental 
    rights must be narrowly tailored and must not have a chilling effect on legitimate 
    speech. The court's emphasis on the need for precision in drafting penal provisions 
    is a welcome development.

    The court's observation that the internet is a medium of virtually pervasive 
    communication has significant implications for future cases involving digital 
    rights. The court's recognition of the transformative nature of the internet 
    and its potential for democratizing information is noteworthy.
    """

    # Correct the small text sample
    if corrector.is_available():
        logger.info("Processing small text sample (should not trigger chunking):")
        corrected_text_small = corrector.correct_text(text_with_errors_small)
        logger.info(f"Original text (small): {text_with_errors_small}")
        logger.info(f"Corrected text (small): {corrected_text_small}")

        logger.info("\nProcessing large text sample (should trigger chunking):")
        corrected_text_large = corrector.correct_text(text_with_errors_large)
        logger.info(f"Original text length (large): {len(text_with_errors_large)} characters")
        logger.info(f"Corrected text length (large): {len(corrected_text_large)} characters")
        logger.info(f"Corrected text (large) first 100 chars: {corrected_text_large[:100]}...")
        logger.info(f"Corrected text (large) last 100 chars: ...{corrected_text_large[-100:]}")
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
