# AU Hub - Student Learning and Collaboration Platform
AU Hub is a student-focused learning and collaboration platform designed for the Amrapali University community. It aims to bring academic resources, student discussions, subject-based groups, quizzes, and practical machine learning experiences together in one platform.

## Project Goals

- Connect students across departments and semesters.
- Create subject-specific groups and doubt-solving discussions.
- Share notes, assignments, and previous-year question papers.
- Practice with quizzes and mock tests.
- Explore practical machine learning features and experiments.
- Support a shared application codebase for web and Android.

## Technology Stack

| Component | Technology |
|---|---|
| Web and Android Application | React Native, Expo, TypeScript |
| Backend API | Python, FastAPI |
| Database | MySQL |
| Machine Learning | Python, NumPy, scikit-learn |

## Project Structure

```text
au-hub/
+-- backend/       # Backend API and services
|   +-- app/       # FastAPI application
|   |   +-- api/   # API routes
|   |   +-- core/  # Core configuration
|   |   +-- db/    # Database integration
|   |   +-- models/# Data models
|   |   +-- repositories/ # Data access logic
|   |   +-- schemas/      # Request and response schemas
|   |   +-- services/     # Business logic
|   |   +-- main.py       # FastAPI application entry point
|   +-- migrations/ # Database migrations
|   +-- tests/      # Backend tests
|   +-- requirements.txt  # Python dependencies
+-- docs/           # Architecture and project documentation
+-- ml/             # Machine learning experiments
+-- .gitignore      # Files and folders excluded from Git
+-- README.md       # Project overview and instructions
```

## Backend Setup

### Prerequisites

- Python 3.10 or a compatible newer version
- Git
- A code editor such as Visual Studio Code

### Run the API Locally

1. Clone the repository and open its directory.
2. Create and activate a Python virtual environment.
3. Install the backend dependencies:

   ```bash
   python -m pip install fastapi "uvicorn[standard]"
   ```

4. Start the development server from the project root:

   ```bash
   python -m uvicorn backend.app.main:app --reload
   ```

5. Open these URLs in your browser:

   - API root: http://127.0.0.1:8000/
   - Health check: http://127.0.0.1:8000/health
   - Interactive API documentation: http://127.0.0.1:8000/docs

The `--reload` option automatically restarts the development server when relevant source files change. It is intended for local development, not production deployment.

## Development Roadmap

1. Establish the backend API foundation.
2. Design the database and student verification workflow.
3. Implement student groups and discussions.
4. Add academic resource sharing and search.
5. Implement quizzes and assessment history.
6. Develop and evaluate the first machine learning feature.
7. Build and test the web and Android applications.
8. Add security testing, documentation, and deployment workflows.

## Security Principles

- Protect student privacy and academic data.
- Enforce authentication and authorization on the backend.
- Restrict access to private academic uploads.
- Never commit passwords, secret keys, or private datasets.
- Validate user input and handle errors safely.
- Evaluate machine learning models before integrating them into the application.

## Current Project Status

The initial repository structure and FastAPI application foundation are in place. The API root and health-check endpoints have been implemented and tested locally. Database integration, student-facing features, machine learning functionality, and the frontend remain part of the development roadmap.

## Contributing

Contributions should be focused, documented, and tested. Use clear commit messages and avoid committing generated files, secrets, or private data.

## License

A project license has not yet been specified.
