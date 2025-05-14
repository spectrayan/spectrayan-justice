"""
Tests for the PDF to JSON converter.

This module contains tests for the PDF to JSON converter classes.
"""

import os
import json
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock, mock_open

from src.config.pdf_converter_config import PDFConverterSettings
from src.utils.pdf2json.pdf_reader import PDFReader
from src.utils.pdf2json.pdf_parser import PDFParser
from src.utils.pdf2json.json_converter import JSONConverter
from src.utils.pdf2json.jsonl_writer import JSONLWriter
from src.utils.pdf2json.pdf_converter import PDFConverter


class TestPDFConverterSettings:
    """Tests for the PDFConverterSettings class."""

    def test_default_settings(self):
        """Test that default settings are created correctly."""
        settings = PDFConverterSettings()
        assert settings.pdf_input_dir == "./data/pdfs"
        assert settings.json_output_dir == "./data/json"
        assert settings.batch_size == 10
        assert settings.use_ai_extraction is False
        assert "id" in settings.field_mappings
        assert "citation" in settings.field_mappings
        assert "act" in settings.field_mappings
        assert "description" in settings.field_mappings
        assert "verdict" in settings.field_mappings
        assert "judgementDate" in settings.field_mappings

    def test_custom_settings(self):
        """Test that custom settings are applied correctly."""
        settings = PDFConverterSettings(
            pdf_input_dir="./custom/input",
            json_output_dir="./custom/output",
            batch_size=5,
            use_ai_extraction=True
        )
        assert settings.pdf_input_dir == "./custom/input"
        assert settings.json_output_dir == "./custom/output"
        assert settings.batch_size == 5
        assert settings.use_ai_extraction is True

    def test_get_paths(self):
        """Test that path getters work correctly."""
        settings = PDFConverterSettings()
        assert isinstance(settings.get_input_path(), Path)
        assert isinstance(settings.get_output_path(), Path)
        assert str(settings.get_input_path()) == "./data/pdfs"
        assert str(settings.get_output_path()) == "./data/json"


class TestPDFReader:
    """Tests for the PDFReader class."""

    @patch('src.utils.pdf2json.pdf_reader.Path.exists')
    @patch('src.utils.pdf2json.pdf_reader.Path.mkdir')
    def test_init_creates_directory(self, mock_mkdir, mock_exists):
        """Test that the reader creates the input directory if it doesn't exist."""
        mock_exists.return_value = False
        reader = PDFReader("./test/input")
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

    @patch('src.utils.pdf2json.pdf_reader.Path.glob')
    def test_get_pdf_files(self, mock_glob):
        """Test that get_pdf_files returns the correct list of files."""
        mock_glob.return_value = [
            Path("./test/input/file1.pdf"),
            Path("./test/input/file2.pdf")
        ]
        reader = PDFReader("./test/input")
        files = reader.get_pdf_files()
        assert len(files) == 2
        assert files[0].name == "file1.pdf"
        assert files[1].name == "file2.pdf"

    @patch('src.utils.pdf2json.pdf_reader.PyMuPDF.open')
    def test_read_pdf(self, mock_pymupdf_open):
        """Test that read_pdf extracts content correctly."""
        # Mock the PyMuPDF.open return value
        mock_doc = MagicMock()
        mock_doc.metadata = {
            "title": "Test Document",
            "author": "Test Author"
        }
        mock_doc.__len__.return_value = 2

        # Mock the pages
        mock_page1 = MagicMock()
        mock_page1.get_text.return_value = "Page 1 content"
        mock_page2 = MagicMock()
        mock_page2.get_text.return_value = "Page 2 content"
        mock_doc.__iter__.return_value = [mock_page1, mock_page2]

        mock_pymupdf_open.return_value = mock_doc

        reader = PDFReader("./test/input")
        result = reader.read_pdf(Path("./test/input/test.pdf"))

        assert "metadata" in result
        assert "content" in result
        assert result["metadata"]["filename"] == "test.pdf"
        assert result["metadata"]["title"] == "Test Document"
        assert result["metadata"]["author"] == "Test Author"
        assert result["metadata"]["page_count"] == 2
        assert result["content"]["page_1"] == "Page 1 content"
        assert result["content"]["page_2"] == "Page 2 content"


class TestPDFParser:
    """Tests for the PDFParser class."""

    def test_parse_pdf_content(self):
        """Test that parse_pdf_content extracts fields correctly."""
        # Create a sample PDF content dictionary
        pdf_content = {
            "metadata": {
                "filename": "test.pdf"
            },
            "content": {
                "page_1": "Case No: 123/2023\nCitation: [2023] Test 123\nAct: Test Act, 2023\n",
                "page_2": "Headnote: This is a test case.\nJUDGMENT\nThis is the verdict.\nDate of Judgment: 15th August, 2023"
            }
        }

        # Create field mappings
        field_mappings = {
            "id": ["Case No", "Case Number", "ID"],
            "citation": ["Citation", "Cite as"],
            "act": ["Act", "Statute", "Law"],
            "description": ["Headnote", "Summary", "Synopsis"],
            "verdict": ["Judgment", "Verdict", "Decision", "Order"],
            "judgementDate": ["Date of Judgment", "Judgment Date", "Date"]
        }

        parser = PDFParser(field_mappings)
        result = parser.parse_pdf_content(pdf_content)

        assert result["source_file"] == "test.pdf"
        assert result["id"] == "123/2023"
        assert "[2023] Test 123" in result["citation"]
        assert "Test Act, 2023" in result["act"]
        assert "This is a test case." in result["description"]
        assert "This is the verdict." in result["verdict"]
        assert result["judgementDate"] == "2023-08-15"

    def test_parse_date(self):
        """Test that _parse_date handles different date formats correctly."""
        parser = PDFParser({})

        # Test different date formats
        assert parser._parse_date("15th August, 2023") == "2023-08-15"
        assert parser._parse_date("15/08/2023") == "2023-08-15"
        assert parser._parse_date("2023/08/15") == "2023-08-15"
        assert parser._parse_date("August 15, 2023") == "2023-08-15"

        # Test invalid date
        assert parser._parse_date("Invalid date") == "Invalid date"


class TestJSONConverter:
    """Tests for the JSONConverter class."""

    def test_convert_to_json(self):
        """Test that convert_to_json creates the correct JSON structure."""
        parsed_data = {
            "source_file": "test.pdf",
            "id": "123/2023",
            "citation": "[2023] Test 123",
            "act": "Test Act, 2023",
            "description": "This is a test case.",
            "verdict": "This is the verdict.",
            "judgementDate": "2023-08-15"
        }

        converter = JSONConverter()
        result = converter.convert_to_json(parsed_data)

        assert result["id"] == "123/2023"
        assert result["citation"] == "[2023] Test 123"
        assert result["act"] == "Test Act, 2023"
        assert result["description"] == "This is a test case."
        assert result["verdict"] == "This is the verdict."
        assert result["judgementDate"] == "2023-08-15"
        assert result["source_file"] == "test.pdf"

    def test_convert_batch_to_json(self):
        """Test that convert_batch_to_json processes a batch correctly."""
        parsed_data_batch = [
            {
                "source_file": "test1.pdf",
                "id": "123/2023",
                "citation": "[2023] Test 123"
            },
            {
                "source_file": "test2.pdf",
                "id": "124/2023",
                "citation": "[2023] Test 124"
            }
        ]

        converter = JSONConverter()
        result = converter.convert_batch_to_json(parsed_data_batch)

        assert len(result) == 2
        assert result[0]["id"] == "123/2023"
        assert result[1]["id"] == "124/2023"


class TestJSONLWriter:
    """Tests for the JSONLWriter class."""

    @patch('src.utils.pdf2json.jsonl_writer.Path.exists')
    @patch('src.utils.pdf2json.jsonl_writer.Path.mkdir')
    def test_init_creates_directory(self, mock_mkdir, mock_exists):
        """Test that the writer creates the output directory if it doesn't exist."""
        mock_exists.return_value = False
        writer = JSONLWriter("./test/output")
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_jsonl(self, mock_file):
        """Test that write_jsonl writes data correctly."""
        json_data = [
            {"id": "123", "citation": "Test 123"},
            {"id": "124", "citation": "Test 124"}
        ]

        writer = JSONLWriter("./test/output")
        writer.write_jsonl(json_data, "test.jsonl")

        # Check that the file was opened for writing
        mock_file.assert_called_once_with(Path("./test/output/test.jsonl"), 'w', encoding='utf-8')

        # Check that the data was written correctly
        handle = mock_file()
        assert handle.write.call_count == 2

        # Check the content of the writes
        calls = handle.write.call_args_list
        assert json.loads(calls[0][0].split('\n')[0]) == json_data[0]
        assert json.loads(calls[1][0].split('\n')[0]) == json_data[1]

    @patch('builtins.open', new_callable=mock_open)
    def test_append_jsonl(self, mock_file):
        """Test that append_jsonl appends data correctly."""
        json_data = {"id": "123", "citation": "Test 123"}

        writer = JSONLWriter("./test/output")
        writer.append_jsonl(json_data, "test.jsonl")

        # Check that the file was opened for appending
        mock_file.assert_called_once_with(Path("./test/output/test.jsonl"), 'a', encoding='utf-8')

        # Check that the data was written correctly
        handle = mock_file()
        handle.write.assert_called_once()

        # Check the content of the write
        call = handle.write.call_args[0][0]
        assert json.loads(call.split('\n')[0]) == json_data


class TestPDFConverter:
    """Tests for the PDFConverter class."""

    def test_init_with_default_settings(self):
        """Test that the converter initializes with default settings."""
        converter = PDFConverter()
        assert isinstance(converter.settings, PDFConverterSettings)
        assert isinstance(converter.reader, PDFReader)
        assert isinstance(converter.parser, PDFParser)
        assert isinstance(converter.converter, JSONConverter)
        assert isinstance(converter.writer, JSONLWriter)

    def test_init_with_custom_settings(self):
        """Test that the converter initializes with custom settings."""
        settings = PDFConverterSettings(
            pdf_input_dir="./custom/input",
            json_output_dir="./custom/output"
        )
        converter = PDFConverter(settings)
        assert converter.settings.pdf_input_dir == "./custom/input"
        assert converter.settings.json_output_dir == "./custom/output"

    @patch('src.utils.pdf2json.pdf_reader.PDFReader.read_pdf')
    @patch('src.utils.pdf2json.pdf_parser.PDFParser.parse_pdf_content')
    @patch('src.utils.pdf2json.json_converter.JSONConverter.convert_to_json')
    def test_convert_pdf(self, mock_convert, mock_parse, mock_read):
        """Test that convert_pdf calls the component methods correctly."""
        # Set up mocks
        mock_read.return_value = {"metadata": {"filename": "test.pdf"}, "content": {}}
        mock_parse.return_value = {"id": "123"}
        mock_convert.return_value = {"id": "123", "formatted": True}

        # Create converter and call method
        converter = PDFConverter()
        result = converter.convert_pdf("test.pdf")

        # Check that the component methods were called
        mock_read.assert_called_once()
        mock_parse.assert_called_once_with({"metadata": {"filename": "test.pdf"}, "content": {}})
        mock_convert.assert_called_once_with({"id": "123"})

        # Check the result
        assert result == {"id": "123", "formatted": True}

    @patch('src.utils.pdf2json.pdf_converter.PDFConverter.convert_pdf')
    @patch('src.utils.pdf2json.jsonl_writer.JSONLWriter.write_jsonl')
    def test_convert_pdf_to_jsonl(self, mock_write, mock_convert):
        """Test that convert_pdf_to_jsonl calls the component methods correctly."""
        # Set up mocks
        mock_convert.return_value = {"id": "123"}
        mock_write.return_value = "./output/test.jsonl"

        # Create converter and call method
        converter = PDFConverter()
        result = converter.convert_pdf_to_jsonl("test.pdf")

        # Check that the component methods were called
        mock_convert.assert_called_once_with(Path("test.pdf"))
        mock_write.assert_called_once_with([{"id": "123"}], "test.jsonl")

        # Check the result
        assert result == "./output/test.jsonl"

    @patch('src.utils.pdf2json.pdf_reader.PDFReader.read_pdfs_batch')
    @patch('src.utils.pdf2json.pdf_parser.PDFParser.parse_pdf_content')
    @patch('src.utils.pdf2json.json_converter.JSONConverter.convert_batch_to_json')
    @patch('src.utils.pdf2json.jsonl_writer.JSONLWriter.get_output_path')
    @patch('src.utils.pdf2json.jsonl_writer.JSONLWriter.append_jsonl')
    def test_convert_directory(self, mock_append, mock_get_path, mock_convert_batch, mock_parse, mock_read_batch):
        """Test that convert_directory processes batches correctly."""
        # Set up mocks
        mock_path = MagicMock()
        mock_path.exists.return_value = False
        mock_get_path.return_value = mock_path

        mock_read_batch.return_value = [
            [{"metadata": {"filename": "test1.pdf"}, "content": {}}],
            [{"metadata": {"filename": "test2.pdf"}, "content": {}}]
        ]

        mock_parse.side_effect = [{"id": "123"}, {"id": "124"}]
        mock_convert_batch.side_effect = [[{"id": "123"}], [{"id": "124"}]]
        mock_append.return_value = "./output/cases.jsonl"

        # Create converter and call method
        converter = PDFConverter()
        result = converter.convert_directory()

        # Check that the component methods were called
        assert mock_read_batch.call_count == 1
        assert mock_parse.call_count == 2
        assert mock_convert_batch.call_count == 2
        assert mock_append.call_count == 2

        # Check the result
        assert result == "./output/cases.jsonl"


if __name__ == "__main__":
    pytest.main(["-v", "test_pdf_converter.py"])
