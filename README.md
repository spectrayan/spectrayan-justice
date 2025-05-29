# Spectrayan Justice System

An AI-powered justice system platform that integrates judicial processes, evidence management, and AI analysis capabilities.

## Project Overview

The Spectrayan Justice System is a comprehensive platform designed to modernize and streamline judicial processes. It combines traditional case management with advanced AI capabilities to assist in legal analysis, evidence processing, and decision support.

## Project Structure

This project is organized into several modules, each with its own specific purpose:

### [Justice System OpenAPI](./justice-system-openapi/README.md)

The OpenAPI module contains the API specifications that define the data models and endpoints for the entire system. It serves as the central contract between all components and generates code for other modules.

### [Justice System Web](./justice-system-web/README.md)

The web frontend module provides a user interface for interacting with the justice system. It uses Angular and includes automatically generated components based on the OpenAPI specifications.

### [Justice System AI](./justice-system-ai/README.md)

The AI module provides intelligent analysis capabilities for legal cases, including entity extraction, case summarization, and predictive analytics.

## Build Commands

### Generate Angular Components, Forms and Models

```bash
mvn clean generate-sources -pl justice-system-openapi -am -P custom-frontend
```

### Generate Python Models

```bash
mvn clean generate-sources -pl justice-system-openapi -am -P python-models
```

## Getting Started

1. Clone the repository
2. Generate the required code using the build commands above
3. Follow the setup instructions in each module's README

## Contributing

We welcome contributions to the Spectrayan Justice System! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and suggest improvements.

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive environment for all contributors and participants.

## Security

If you discover a security vulnerability, please follow our [Security Policy](SECURITY.md) for responsible disclosure.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
