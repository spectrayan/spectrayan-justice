"""
Tests for the CLI module.
"""
import os
import sys
from unittest.mock import patch

import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from justice_system.cli import main, parse_args


class TestParseArgs:
    """Tests for the parse_args function."""

    def test_analyze_command(self):
        """Test parsing the analyze command."""
        args = parse_args(["analyze", "test.txt", "--model", "custom-model"])
        assert args.command == "analyze"
        assert args.file == "test.txt"
        assert args.model == "custom-model"

    def test_summarize_command(self):
        """Test parsing the summarize command."""
        args = parse_args(["summarize", "test.txt", "--max-length", "100"])
        assert args.command == "summarize"
        assert args.file == "test.txt"
        assert args.max_length == 100

    def test_entities_command(self):
        """Test parsing the entities command."""
        args = parse_args(["entities", "test.txt"])
        assert args.command == "entities"
        assert args.file == "test.txt"
        assert args.model == "default"  # Default value


class TestMain:
    """Tests for the main function."""

    def test_no_command(self):
        """Test running with no command."""
        with patch("sys.stdout"):  # Suppress output
            exit_code = main([])
            assert exit_code == 1

    def test_file_not_found(self):
        """Test running with a non-existent file."""
        with patch("sys.stdout"):  # Suppress output
            exit_code = main(["analyze", "nonexistent.txt"])
            assert exit_code == 1

    def test_analyze_command(self):
        """Test running the analyze command with a real file."""
        # Get the path to the sample case file
        sample_file = os.path.join(
            os.path.dirname(__file__), "data", "sample_case.txt"
        )

        # Make sure the file exists
        assert os.path.exists(sample_file), f"Sample file not found: {sample_file}"

        with patch("sys.stdout"):  # Suppress output
            exit_code = main(["analyze", sample_file])
            assert exit_code == 0

    def test_summarize_command(self):
        """Test running the summarize command with a real file."""
        # Get the path to the sample case file
        sample_file = os.path.join(
            os.path.dirname(__file__), "data", "sample_case.txt"
        )

        with patch("sys.stdout"):  # Suppress output
            exit_code = main(["summarize", sample_file, "--max-length", "100"])
            assert exit_code == 0

    def test_entities_command(self):
        """Test running the entities command with a real file."""
        # Get the path to the sample case file
        sample_file = os.path.join(
            os.path.dirname(__file__), "data", "sample_case.txt"
        )

        with patch("sys.stdout"):  # Suppress output
            exit_code = main(["entities", sample_file, "--model", "custom-model"])
            assert exit_code == 0
