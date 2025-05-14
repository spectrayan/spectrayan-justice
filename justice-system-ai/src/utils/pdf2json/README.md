# PDF to JSON Converter

A Python module for converting PDF files to JSON and JSONL format, with a focus on extracting structured information from legal documents.

## Features

- Convert PDF files to JSON format with structured fields
- Extract key information like case ID, citation, act, description, verdict, and judgment date
- Properly handle multi-line content in fields, reading until the next section is reached
- Intelligently distinguish between "DATE OF JUDGMENT" and "JUDGMENT" sections
- Replace newline characters with spaces in extracted fields for cleaner output
- Automatically remove page headers, footers, page numbers, and URLs from the extracted text
- Process PDFs in batches for efficient handling of large collections
- Write output to JSONL files for easy integration with other systems
- Configurable field mappings to adapt to different document formats
- AI-enhanced text correction to fix spelling and grammar errors in extracted text
- Anonymization of names by replacing individuals and entities with appropriate role-based terms
- Uses LlamaIndex and Ollama for high-quality text correction and anonymization

## Components

The module is organized into several classes, each with a specific responsibility:

- **PDFReader**: Reads PDF files and extracts their raw content using PyMuPDF
- **PDFParser**: Parses the raw PDF content and extracts structured information
- **TextCorrector**: Corrects spelling and grammar in extracted text and anonymizes names of individuals and entities using LlamaIndex and Ollama
- **JSONConverter**: Converts parsed data to standardized JSON format
- **JSONLWriter**: Writes JSON data to JSONL files
- **PDFConverter**: Main class that orchestrates the conversion process

## Usage

### Basic Usage

```python
from src.utils import PDFConverter
from src.config.pdf_converter_config import PDFConverterSettings

# Create a converter with default settings
converter = PDFConverter()

# Convert a single PDF file
json_data = converter.convert_pdf("path/to/document.pdf")

# Convert a single PDF file and write to JSONL
output_path = converter.convert_pdf_to_jsonl("path/to/document.pdf")

# Convert all PDFs in the input directory
output_path = converter.convert_directory(output_filename="cases.jsonl")
```

The `convert_directory` method includes robust error handling that catches any exceptions during processing, logs them, and continues with the next file. It also automatically skips PDFs with empty or null content. This ensures that the conversion process doesn't stop if there are issues with individual files or if it encounters empty PDFs.

### Custom Settings

```python
# Create custom settings
custom_settings = PDFConverterSettings(
    pdf_input_dir="./custom/input/dir",
    json_output_dir="./custom/output/dir",
    batch_size=5,
    use_ai_extraction=True,
    text_correction_model="llama2",
    text_correction_temperature=0.1
)

# Create a converter with custom settings
converter = PDFConverter(custom_settings)

# Convert PDFs using custom settings
output_path = converter.convert_directory(output_filename="custom_cases.jsonl")
```

### Text Correction and Anonymization

The module includes AI-powered text correction to fix spelling and grammar errors in extracted text and anonymize names of individuals and entities:

```python
# Enable AI-enhanced text correction and anonymization
converter.convert_with_ai(True)

# Convert a PDF with text correction and anonymization
json_data = converter.convert_pdf("path/to/document.pdf")
```

You can also use the TextCorrector directly:

```python
from src.utils.pdf2json.text_corrector import TextCorrector

# Create a text corrector
corrector = TextCorrector(model_name="llama2", temperature=0.1)

# Correct a single text string and anonymize names
corrected_text = corrector.correct_text("Text with speling and grammer errors mentioning John Smith and ABC Corporation")

# Correct multiple fields in a dictionary and anonymize names
data = {
    "description": "Summary with speling errors about Jane Doe and XYZ Ltd.",
    "verdict": "Judgement with grammer mistakes involving Mr. Johnson and Acme Inc."
}
corrected_data = corrector.correct_fields(data, fields_to_correct=["description", "verdict"])
```

The anonymization process replaces names of individuals and entities with appropriate role-based terms:
- Individual names (e.g., "John Smith", "Jane Doe") are replaced with terms like defendant, accused, petitioner, appellant, respondent, witness, victim, complainant, lawyer, attorney, counsel, advocate, judge, magistrate, etc.
- Organization names (e.g., "ABC Corporation", "XYZ Ltd.") are replaced with terms like organization, company, corporation, institution, etc.

This helps protect privacy while maintaining the context and meaning of the text.

### Header Removal

The module automatically removes common headers, footers, page numbers, and URLs from the extracted text:

```python
# Headers are automatically removed during PDF parsing
# The following types of headers are removed:
# - Court names (e.g., "SUPREME COURT OF INDIA", "HIGH COURT OF [STATE]") 
#   ONLY if they appear in the same line as "Page X of Y" pattern
# - URLs in headers (e.g., "http://JUDIS.NIC.IN") - always removed
# - Page numbers in various formats - always removed
# - Copyright and courtesy notices - always removed
# - Printed for/from lines - always removed
```

The header removal is performed on each page before the content is combined for field extraction. This ensures that the extracted fields don't contain irrelevant header information. The system intelligently handles headers that may be split across multiple lines by concatenating groups of lines before checking for patterns. Court names like "SUPREME COURT OF INDIA" or "HIGH COURT OF [STATE]" are only removed if they appear with a "Page X of Y" pattern in the same group of lines, preserving these important identifiers when they appear in the main content.

### Field Mappings

The converter uses field mappings to identify and extract information from the PDF. The default mappings are:

```python
field_mappings = {
    "id": ["Case No", "Case Number", "ID"],
    "citation": ["Citation", "Cite as"],
    "act": ["Act", "Statute", "Law"],
    "description": ["Headnote", "Summary", "Synopsis"],
    "verdict": ["Judgment", "Verdict", "Decision", "Order"],
    "judgementDate": ["Date of Judgment", "Judgment Date", "Date"]
}
```

You can customize these mappings in your PDFConverterSettings:

```python
custom_settings = PDFConverterSettings(
    field_mappings={
        "id": ["Case No", "Case Number", "ID", "Case ID"],
        # Add other custom mappings...
    }
)
```

## Installation Requirements

The module requires the following dependencies:

- PyMuPDF: For reading and extracting content from PDF files
- Pydantic: For settings validation and management
- LlamaIndex: For AI-powered text correction
- Ollama: For running local language models

Install the dependencies using pip:

```bash
pip install pymupdf pydantic llama-index
```

Additionally, you need to install and run Ollama:

1. Install Ollama from [https://ollama.ai/](https://ollama.ai/)
2. Pull the llama2 model (or another model of your choice):
   ```bash
   ollama pull llama2
   ```
3. Make sure the Ollama service is running before using the text correction functionality

## Examples

- See the `examples/pdf_converter_example.py` script for a complete example of how to use the PDF converter.
- See the `examples/text_correction_example.py` script for examples of how to use the text correction functionality.

## Testing

The module includes comprehensive tests in `tests/test_pdf_converter.py`. Run the tests using pytest:

```bash
pytest tests/test_pdf_converter.py
```
