# Justice System Web

This is the web frontend for the Spectrayan Justice System project. It provides a user interface for interacting with the justice system APIs and visualizing data.

This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 19.2.1.

## Development server

To start a local development server, run:

```bash
ng serve
```

Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Karma](https://karma-runner.github.io) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Key Features

- **User Interface for Justice System**: Provides interfaces for managing cases, evidence, and judicial entities
- **Generated Components**: Uses automatically generated Angular components based on OpenAPI specifications
- **Form Components**: Includes form components for data entry and editing
- **Responsive Design**: Works on desktop and mobile devices

## Integration with Other Modules

This module integrates with other parts of the Spectrayan Justice System:

- **justice-system-openapi**: The OpenAPI module generates TypeScript models, interfaces, and Angular form components in the `src/app/generated` directory. These are used to ensure type safety and consistent data structures.

- **justice-system-ai**: Communicates with the AI module through the API to leverage AI-powered features.

### Generating Angular Components

To update the generated components after changes to the OpenAPI specifications:

```bash
# From the project root
mvn clean generate-sources -pl justice-system-openapi -am -P custom-frontend
```

## Project Structure

```
justice-system-web/
├── src/
│   ├── app/
│   │   ├── components/     # Custom Angular components
│   │   ├── generated/      # Generated components from OpenAPI
│   │   │   ├── form-components/  # Generated form components
│   │   │   └── model/      # Generated TypeScript models
│   │   ├── pages/          # Page components
│   │   └── services/       # Angular services
│   ├── assets/             # Static assets
│   └── environments/       # Environment configurations
└── angular.json           # Angular configuration
```

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
