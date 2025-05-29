# Contributing to Spectrayan Justice System

Thank you for your interest in contributing to the Spectrayan Justice System! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Environment Setup](#development-environment-setup)
- [Contribution Workflow](#contribution-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Issue and Pull Request Process](#issue-and-pull-request-process)
- [Module-Specific Guidelines](#module-specific-guidelines)

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md). We expect all contributors to adhere to this code to ensure a positive and respectful environment for everyone.

## Getting Started

1. Fork the repository
2. Clone your fork to your local machine
3. Set up the development environment as described below
4. Create a new branch for your changes
5. Make your changes and commit them
6. Push your changes to your fork
7. Submit a pull request

## Development Environment Setup

### Prerequisites

- Java 17 or higher
- Maven 3.8 or higher
- Node.js 18 or higher and npm
- Python 3.10 or higher
- uv (Python package manager)

### Setting Up the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spectrayan-justice.git
   cd spectrayan-justice
   ```

2. Generate the required code:
   ```bash
   # Generate Angular components
   mvn clean generate-sources -pl justice-system-openapi -am -P custom-frontend
   
   # Generate Python models
   mvn clean generate-sources -pl justice-system-openapi -am -P python-models
   ```

3. Set up the web module:
   ```bash
   cd justice-system-web
   npm install
   ```

4. Set up the AI module:
   ```bash
   cd justice-system-ai
   uv pip install -e ".[dev]"
   ```

## Contribution Workflow

1. **Create an Issue**: Before making significant changes, create an issue to discuss the proposed changes.
2. **Branch Naming**: Use descriptive branch names with prefixes:
   - `feature/` for new features
   - `bugfix/` for bug fixes
   - `docs/` for documentation changes
   - `refactor/` for code refactoring
3. **Commit Messages**: Write clear, concise commit messages that explain the changes made.
4. **Pull Requests**: Submit a pull request with a clear description of the changes and reference to the related issue.

## Coding Standards

### Java
- Follow the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- Use meaningful variable and method names
- Include JavaDoc comments for public methods and classes

### TypeScript/Angular
- Follow the [Angular Style Guide](https://angular.io/guide/styleguide)
- Use TypeScript's strict mode
- Ensure components are properly documented

### Python
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints
- Format code with Black and isort
- Run mypy for type checking

## Testing Guidelines

- Write unit tests for all new features and bug fixes
- Ensure all tests pass before submitting a pull request
- Aim for high test coverage

### Running Tests

```bash
# Java/Maven tests
mvn test

# Angular tests
cd justice-system-web
ng test

# Python tests
cd justice-system-ai
pytest
```

## Documentation

- Update documentation for any changes to APIs, features, or behavior
- Document new features thoroughly
- Keep README files up to date
- Use clear, concise language in documentation

## Issue and Pull Request Process

### Issues
- Use the issue templates when available
- Provide clear steps to reproduce bugs
- Include expected and actual behavior for bug reports
- For feature requests, explain the use case and benefits

### Pull Requests
- Reference related issues in the PR description
- Provide a clear description of the changes
- Include screenshots for UI changes
- Ensure all CI checks pass
- Request reviews from relevant team members

## Module-Specific Guidelines

### OpenAPI Module
- Maintain backward compatibility when possible
- Document all schema changes
- Run code generation after changes to verify they work

### Web Module
- Follow Angular best practices
- Ensure responsive design
- Test on multiple browsers

### AI Module
- Document model assumptions and limitations
- Include performance metrics for new models
- Provide example usage for new features

## Questions?

If you have any questions or need help, please open an issue or contact the project maintainers.

Thank you for contributing to the Spectrayan Justice System!
