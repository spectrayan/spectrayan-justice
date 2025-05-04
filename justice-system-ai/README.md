# Justice System AI

A Python package providing AI-powered tools and utilities for justice systems. This module is part of the larger Spectrayan Justice System project and works with models generated from the OpenAPI specifications.

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for building and package management.

```bash
# Install uv if you don't have it
pip install uv

# Install the package
uv pip install -e .
```

## Project Structure

```
justice-system-ai/
├── src/                    # Source directory
│   └── justice_system/     # Main package
│       ├── __init__.py
│       ├── cli.py          # Command-line interface
│       └── judicial/       # Judicial submodule
│           ├── __init__.py
│           └── case_analysis.py
├── examples/               # Example scripts
│   └── analyze_case.py     # Example case analysis script
├── tests/                  # Test directory
│   ├── __init__.py
│   ├── test_case_analysis.py
│   ├── test_cli.py
│   └── data/               # Test data
│       └── sample_case.txt
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## Usage

### Python API

```python
from justice_system.judicial.case_analysis import CaseAnalyzer, get_case_summary

# Create a case analyzer
analyzer = CaseAnalyzer(model_name="legal-bert")

# Analyze a case
case_text = "This is a sample legal case text..."
analysis_results = analyzer.analyze_case(case_text)
print(analysis_results)

# Extract entities from case text
entities = analyzer.extract_entities(case_text)
print(entities)

# Get a summary of the case
summary = get_case_summary(case_text, max_length=200)
print(summary)
```

### Command Line Interface

The package also provides a command-line interface for easy access to its functionality:

```bash
# Analyze a legal case
justice-system analyze tests/data/sample_case.txt --model legal-bert

# Generate a summary of a legal case
justice-system summarize tests/data/sample_case.txt --max-length 200

# Extract entities from a legal case
justice-system entities tests/data/sample_case.txt
```

For help with the CLI:

```bash
justice-system --help
```

## Examples

The `examples` directory contains sample scripts that demonstrate how to use the Justice System AI package:

```bash
# Run the analyze_case.py example with the sample case file
python examples/analyze_case.py tests/data/sample_case.txt

# Use a custom model and set maximum summary length
python examples/analyze_case.py tests/data/sample_case.txt --model legal-bert --max-summary-length 150
```

## Development

To set up the development environment:

```bash
# Install development dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/justice_system
isort src/justice_system

# Type checking
mypy src/justice_system
```

## Integration with Other Modules

This module integrates with other parts of the Spectrayan Justice System:

- **justice-system-openapi**: The OpenAPI module generates Python model classes in the `src/generated` directory using the `python-models` Maven profile. These models are used by the AI components to ensure consistent data structures across the system.

- **justice-system-web**: The AI module provides backend processing capabilities that can be called from the web frontend through the API.

To update the generated models after changes to the OpenAPI specifications:

```bash
# From the project root
mvn clean generate-sources -pl justice-system-openapi -am -P python-models
```

## License

MIT
