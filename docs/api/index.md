# API Documentation

This section contains comprehensive documentation for the Eco-Dispose API.

## Overview

The Eco-Dispose API is a RESTful service that enables electronic waste management.
The API is organized around resources and uses standard HTTP methods.

## Database Schema

Entity-relationship diagram for the system:

![Database ERD](/docs/diagrams/erd.png)

## Authentication

The API uses session-based authentication with Flask-Login.

See the [Authentication API](auth.md) for more details on login and registration.

## Base URL

- Local development: `http://localhost:5000`

## API Endpoints

- [Authentication](auth.md) - User registration, login, and profile management
- [Devices](devices.md) - Device submission, retrieval, and status updates

## Response Format

API responses follow consistent conventions:

### Content Type

- **Responses:** All responses are in `application/json` format

### Success Responses

Success responses typically include:

- A `message` field with a descriptive success message
- Often a `user` or relevant resource object with data
- HTTP status codes in the 2xx range

Example:

```json
{
  "message": "registered successfully",
  "user": {
    "id": 1,
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com"
  }
}
```

### Error Responses

Error responses typically include:

- A `message` field with a descriptive error message
- An `error` field with additional error details
- HTTP status codes in the 4xx or 5xx range

Example:

```json
{
  "message": "Invalid request",
  "error": "Missing required fields"
}
```

### Status Codes

The API uses conventional HTTP response codes to indicate success or failure:

- `200 OK` - Request succeeded
- `201 Created` - Resource was successfully created
- `400 Bad Request` - Invalid request or parameters
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Authenticated but not authorized
- `404 Not Found` - Resource not found
- `409 Conflict` - Request conflicts with current state
- `500 Internal Server Error` - Server-side error
