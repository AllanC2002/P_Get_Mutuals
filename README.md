# Get Mutual follow Microservice

This document provides an overview of the project structure, backend design, communication architecture, and API endpoint instructions.

## Table of Contents

- [Folder Functions](#folder-functions)
- [Backend Design Pattern](#backend-design-pattern)
- [Communication Architecture](#communication-architecture)
- [Folder Pattern](#folder-pattern)
- [Endpoint Instructions](#endpoint-instructions)
  - [/get-mutuals](#get-mutuals)

## Folder Functions

The project is organized into the following folders:

-   **.github/**: Contains GitHub-specific files.
    -   **.github/workflows/**: Stores GitHub Actions workflow files for CI/CD, such as Docker image building and publishing (`docker-publish.yml`, `docker-publish_qa.yml`).
-   **controllers/**: Handles incoming HTTP requests, processes them, and returns responses. This is where API endpoint logic resides (e.g., `mutuals_controller.py`).
-   **db/**: Manages database interactions, primarily for establishing and managing connections to the MySQL database (e.g., `mysql_connection.py`).
-   **models/**: Contains data models or schema definitions using SQLAlchemy ORM (e.g., `profile_model.py` which defines `Profile` and `Followers` tables).
-   **queries/**: Encapsulates specific database query logic and business operations (e.g., `get_mutual_followers.py`).
-   **tests/**: Contains test files for the application. `routetest.py` includes integration tests for API endpoints.
-   **utils/**: Provides utility functions and helper modules used across the application, such as JWT handling (`jwt_utils.py`).

Key files in the root directory:

-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
-   `app.py`: The main entry point of the Flask application. It initializes the app and registers API blueprints.
-   `dockerfile`: Contains instructions to build a Docker image for the application.
-   `requirements.txt`: Lists the Python dependencies required for the project.

## Backend Design Pattern

The application primarily uses a **CQRS**. This pattern separates concerns into distinct layers:

-   **Presentation Layer (Controllers)**: `controllers/` - Manages HTTP request and response handling.
-   **Business Logic/Service Layer (Queries)**: `queries/` - Contains the core application logic and orchestrates data operations.
-   **Data Access Layer (Models & DB Connection)**: `models/` and `db/` - Defines data structures (ORM models) and manages database connectivity and operations.

This structure is similar to MVC (Model-View-Controller) but adapted for an API backend, where the "View" is the JSON response.

## Communication Architecture

The application employs a **REST API** architecture.

-   Communication is synchronous, following a request-response model over HTTP.
-   Flask is used as the web framework to define and serve API endpoints.
-   JSON is the primary format for data exchange.
-   Authentication is handled via JWT (JSON Web Tokens), passed as Bearer tokens in the `Authorization` header.

## Folder Pattern

The project follows a **layer-based (or role-based) grouping** for its folder structure. Files and modules are organized based on their technical role or responsibility within the application's architecture (e.g., all controllers are in `controllers/`, all data models in `models/`).

## Endpoint Instructions

### `/get-mutuals`

-   **Method:** `GET`
-   **Description:** Retrieves a list of mutual followers for the authenticated user. Mutual followers are users who both follow the authenticated user and are followed by the authenticated user.
-   **Authentication:** Required. Uses JWT Bearer token.
    -   The token must be passed in the `Authorization` header.
    -   Format: `Authorization: Bearer <your_jwt_token>`
-   **Request Headers:**
    -   `Authorization`: (Required) `Bearer <token>`
-   **Request Body:** None
-   **Success Response (200 OK):**
    -   **Content-Type:** `application/json`
    -   **Body:** A JSON array of objects, where each object represents a mutual user.
        *   Example:
            ```json
            [
                {
                    "Id_User": 123,
                    "User_mail": "user@example.com"
                },
                {
                    "Id_User": 456,
                    "User_mail": "anotheruser@example.com"
                }
            ]
            ```
-   **Error Responses:**
    *   **401 Unauthorized:**
        *   If the `Authorization` header is missing, malformed, or the token is invalid or expired.
        *   **Content-Type:** `application/json`
        *   **Body Example:**
            ```json
            {
                "error": "Token missing or invalid"
            }
            ```

**Note on obtaining the JWT Token:**
To use the `/get-mutuals` endpoint, a client must first obtain a JWT token. The test script (`tests/routetest.py`) suggests this token is acquired from a `/login` endpoint (details not provided in the current controller code). Typically, this involves sending credentials (e.g., email and password) to the login endpoint and receiving the token in response.
