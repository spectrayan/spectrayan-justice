"""
Tests for the case_analysis module.
"""
import pytest

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from justice_system.judicial.case_analysis import CaseAnalyzer, get_case_summary


class TestCaseAnalyzer:
    """Tests for the CaseAnalyzer class."""

    def test_init(self):
        """Test initialization with default and custom model names."""
        # Test with default model name
        analyzer = CaseAnalyzer()
        assert analyzer.model_name == "default"

        # Test with custom model name
        custom_analyzer = CaseAnalyzer(model_name="custom-model")
        assert custom_analyzer.model_name == "custom-model"

    def test_analyze_case(self):
        """Test the analyze_case method."""
        analyzer = CaseAnalyzer()
        case_text = "This is a sample case text for testing."

        result = analyzer.analyze_case(case_text)

        # Check that the result is a dictionary
        assert isinstance(result, dict)

        # Check that the expected keys are present
        assert "summary" in result
        assert "key_points" in result
        assert "sentiment" in result
        assert "precedents" in result
        assert "model_used" in result

        # Check that the model_used matches the analyzer's model_name
        assert result["model_used"] == analyzer.model_name

        # Check that the summary contains the length of the case text
        assert str(len(case_text)) in result["summary"]

    def test_extract_entities(self):
        """Test the extract_entities method."""
        analyzer = CaseAnalyzer()
        case_text = "John Doe appeared before the Supreme Court on January 1, 2023."

        entities = analyzer.extract_entities(case_text)

        # Check that the result is a list
        assert isinstance(entities, list)

        # Check that we have at least one entity
        assert len(entities) > 0

        # Check that each entity has the expected keys
        for entity in entities:
            assert "type" in entity
            assert "text" in entity
            assert "confidence" in entity


def test_get_case_summary():
    """Test the get_case_summary function."""
    case_text = "This is a sample case text for testing."

    # Test without max_length
    summary = get_case_summary(case_text)
    assert isinstance(summary, str)
    assert str(len(case_text)) in summary

    # Test with max_length that doesn't truncate
    long_enough = 100
    summary_long = get_case_summary(case_text, max_length=long_enough)
    assert len(summary_long) <= long_enough
    assert not summary_long.endswith("...")

    # Test with max_length that does truncate
    too_short = 10
    summary_short = get_case_summary(case_text, max_length=too_short)
    assert len(summary_short) <= too_short + 3  # +3 for "..."
    assert summary_short.endswith("...")
