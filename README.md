# FastAPI Login Service

A production-level FastAPI backend providing authentication, login, and signup functionalities.

## Features

- **FastAPI**: Modern, fast web framework
- **SQLAlchemy (MySQL)**: Mature ORM for interacting with the database
- **JWT Authentication**: Complete OAuth2 flow using JSON Web Tokens
- **Password Hashing**: Bcrypt encryption for passwords
- **Dockerized**: Easy setup using Docker & Docker Compose
- **Environment Driven**: Secrets and configurations are loaded completely via the `.env` file, ensuring sensitive data is not hardcoded.

## Prerequisites

- Docker
- Docker Compose

## Quick Start
1. Ensure the `.env` file is present in the root directory (a sample has been provided for local development).
2. Start the services using Docker Compose:
```bash
docker compose up -d --build
```
3. The API will be available at `http://localhost:8000`. You can visit the auto-generated Swagger documentation UI directly at `http://localhost:8000/docs` to test endpoints like `Signup`, `Login`, and fetching current user info `Me`.

## Project Structure
- `app/api`: Defines endpoints and route dependencies.
- `app/core`: Configuration management and security utilities.
- `app/db`: Database connection models and initialization.
- `app/schemas`: Pydantic models used as schemas corresponding to API payload structures.

## Usage Note

The authentication endpoint `/api/auth/login` complies with the `OAuth2PasswordRequestForm` structure, which inherently mandates form fields `username` and `password`. In this application's context, the `username` field accepts the user's `email`.
