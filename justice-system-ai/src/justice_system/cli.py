"""
Command-line interface for the Justice System AI.

This module provides a command-line interface for using the functionality
of the Justice System AI package.
"""
import argparse
import sys
from typing import List, Optional

from justice_system.judicial.case_analysis import CaseAnalyzer, get_case_summary


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.

    Args:
        args: Command-line arguments. Defaults to sys.argv[1:].

    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Justice System AI - Tools for legal analysis"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Analyze case command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a legal case")
    analyze_parser.add_argument("file", help="Path to the case file to analyze")
    analyze_parser.add_argument(
        "--model", default="default", help="Name of the model to use for analysis"
    )

    # Summarize case command
    summarize_parser = subparsers.add_parser("summarize", help="Summarize a legal case")
    summarize_parser.add_argument("file", help="Path to the case file to summarize")
    summarize_parser.add_argument(
        "--max-length", type=int, help="Maximum length of the summary"
    )

    # Extract entities command
    entities_parser = subparsers.add_parser(
        "entities", help="Extract entities from a legal case"
    )
    entities_parser.add_argument("file", help="Path to the case file to extract entities from")
    entities_parser.add_argument(
        "--model", default="default", help="Name of the model to use for extraction"
    )

    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> int:
    """
    Main entry point for the CLI.

    Args:
        args: Command-line arguments. Defaults to sys.argv[1:].

    Returns:
        Exit code.
    """
    parsed_args = parse_args(args)

    if not parsed_args.command:
        print("Error: No command specified. Use --help for usage information.")
        return 1

    try:
        # Read the case file
        with open(parsed_args.file, "r", encoding="utf-8") as f:
            case_text = f.read()

        if parsed_args.command == "analyze":
            analyzer = CaseAnalyzer(model_name=parsed_args.model)
            results = analyzer.analyze_case(case_text)

            print(f"Analysis Results (using model: {results['model_used']}):")
            print(f"Summary: {results['summary']}")
            print("Key Points:")
            for point in results["key_points"]:
                print(f"- {point}")
            print(f"Sentiment: {results['sentiment']}")
            print("Precedents:")
            for precedent in results["precedents"]:
                print(f"- {precedent}")

        elif parsed_args.command == "summarize":
            summary = get_case_summary(case_text, max_length=parsed_args.max_length)
            print(f"Case Summary:\n{summary}")

        elif parsed_args.command == "entities":
            analyzer = CaseAnalyzer(model_name=parsed_args.model)
            entities = analyzer.extract_entities(case_text)

            print(f"Entities Extracted (using model: {parsed_args.model}):")
            for entity in entities:
                print(f"- {entity['type']}: {entity['text']} (confidence: {entity['confidence']})")

        return 0

    except FileNotFoundError:
        print(f"Error: File not found: {parsed_args.file}")
        return 1
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
