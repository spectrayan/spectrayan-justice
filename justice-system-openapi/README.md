# Justice System OpenAPI

This module contains the OpenAPI specifications for the Justice System project. It serves as the central definition of the API contract between different components of the system.

## Overview

The Justice System OpenAPI module defines the structure, endpoints, and data models for the entire Justice System application. It uses the OpenAPI 3.0 specification format to describe the API in a standardized way.

## Key Features

- **Centralized API Definition**: Single source of truth for all API contracts
- **Code Generation**: Automatically generates code for multiple platforms
- **Validation**: Ensures API requests and responses conform to the defined schema
- **Documentation**: Self-documenting API specifications

## Project Structure

```
justice-system-openapi/
├── src/
│   └── main/
│       ├── java/           # Empty - no Java code in this module
│       └── resources/
│           ├── components/ # API components (schemas, parameters, etc.)
│           │   └── schemas/
│           │       ├── common/     # Common schema definitions
│           │       ├── corrections/ # Corrections-related schemas
│           │       ├── judicial/   # Judicial system schemas
│           │       └── law-enforcement/ # Law enforcement schemas
│           ├── config/     # Configuration for code generators
│           ├── paths/      # API path definitions
│           │   ├── corrections/    # Corrections-related endpoints
│           │   ├── judicial/       # Judicial system endpoints
│           │   └── law-enforcement/ # Law enforcement endpoints
│           └── justice-system-v1.yaml # Main OpenAPI specification file
└── pom.xml                # Maven build configuration
```

## Code Generation

This module is used to generate code for various parts of the Justice System project:

### Backend Server Code

```bash
mvn clean generate-sources -pl justice-system-openapi -am -P backend-server
```

Generates Spring Boot server code in the `justice-system-apis` module.

### Custom API Code

```bash
mvn clean generate-sources -pl justice-system-openapi -am -P justice-system-api
```

Generates custom API code in the `justice-system-openapi-codegen` module.

### Angular Frontend Components

```bash
mvn clean generate-sources -pl justice-system-openapi -am -P custom-frontend
```

Generates Angular components, forms, and models in the `justice-system-web` module.

### Python Models

```bash
mvn clean generate-sources -pl justice-system-openapi -am -P python-models
```

Generates Python model classes in the `justice-system-ai` module.

## Integration with Other Modules

- **justice-system-web**: Consumes generated TypeScript models and Angular components
- **justice-system-ai**: Uses generated Python models for AI processing
- **justice-system-apis**: Implements the API endpoints defined in this specification

## Development

When making changes to the API specification:

1. Modify the relevant YAML files in the `src/main/resources` directory
2. Run the appropriate code generation command to update dependent modules
3. Test the changes in the affected modules

## Dependencies

- OpenAPI Generator (v7.12.0)
- Maven
- Jackson libraries for YAML/JSON processing
