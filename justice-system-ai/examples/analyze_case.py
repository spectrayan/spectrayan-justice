#!/usr/bin/env python
"""
Example script demonstrating how to use the Justice System AI package.

This script reads a legal case file and performs analysis on it using
the Justice System AI package.
"""
import argparse
import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from justice_system.judicial.case_analysis import CaseAnalyzer, get_case_summary


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Analyze a legal case using Justice System AI"
    )
    parser.add_argument("file", help="Path to the case file to analyze")
    parser.add_argument(
        "--model", default="default", help="Name of the model to use for analysis"
    )
    parser.add_argument(
        "--max-summary-length",
        type=int,
        default=200,
        help="Maximum length of the case summary",
    )
    return parser.parse_args()


def main():
    """Main function."""
    args = parse_args()

    try:
        # Read the case file
        with open(args.file, "r", encoding="utf-8") as f:
            case_text = f.read()

        print(f"Analyzing case file: {args.file}")
        print(f"Using model: {args.model}")
        print("-" * 50)

        # Create a case analyzer
        analyzer = CaseAnalyzer(model_name=args.model)

        # Get a summary of the case
        print("Case Summary:")
        summary = get_case_summary(case_text, max_length=args.max_summary_length)
        print(summary)
        print("-" * 50)

        # Analyze the case
        print("Case Analysis:")
        analysis = analyzer.analyze_case(case_text)

        print(f"Summary: {analysis['summary']}")
        print("Key Points:")
        for point in analysis["key_points"]:
            print(f"- {point}")
        print(f"Sentiment: {analysis['sentiment']}")
        print("Precedents:")
        for precedent in analysis["precedents"]:
            print(f"- {precedent}")
        print("-" * 50)

        # Extract entities from the case
        print("Entities:")
        entities = analyzer.extract_entities(case_text)

        for entity in entities:
            print(f"- {entity['type']}: {entity['text']} (confidence: {entity['confidence']})")

        return 0

    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        return 1
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
