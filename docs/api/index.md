# API Documentation

<div align="center">
  <img src="https://img.shields.io/badge/Eco--Dispose-API%20Documentation-4F46E5?style=for-the-badge&labelColor=000000" alt="Eco-Dispose API Documentation" width="80%"/>
  <br><br>
  <p>
    <img src="https://img.shields.io/badge/Status-Production-brightgreen?style=flat-square" alt="Status: Production"/>
    <img src="https://img.shields.io/badge/Version-1.0-blue?style=flat-square" alt="Version: 1.0"/>
    <img src="https://img.shields.io/badge/Updated-2025--04--14-orange?style=flat-square" alt="Updated: 2025-04-13"/>
  </p>
</div>

---

## Overview

The Eco-Dispose API is a RESTful service that enables electronic waste management.
The API is organized around resources and uses standard HTTP methods.

## Base URL

- Local development: `http://localhost:5000`

## API Endpoints

- [Authentication](auth.md) - User registration, login, and profile management
- [Devices](devices.md) - Device submission, retrieval, and status updates

## Authentication

The API uses session-based authentication with Flask-Login.

See the [Authentication API](auth.md) for more details on login and registration.

## Database Schema

Entity-relationship diagram for the system:

![Database ERD](/docs/diagrams/erd.png)

## Technology Stack

The Eco-Dispose platform is built with the following technologies:

- **Frontend**: Vue.js (82.5%)
- **Backend**: Python/Flask (11.7%)
- **Auxiliary Scripts**: JavaScript (4.4%)
- **Configuration & Other**: (1.4%)

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

| Status Code | Meaning      | Description                                                       |
| ----------- | ------------ | ----------------------------------------------------------------- |
| 200         | OK           | Request was successful                                            |
| 201         | Created      | Resource created successfully                                     |
| 400         | Bad Request  | Missing or invalid parameters                                     |
| 401         | Unauthorized | Authentication required                                           |
| 403         | Forbidden    | User lacks permission for the requested operation                 |
| 404         | Not Found    | Resource not found                                                |
| 409         | Conflict     | Request conflicts with current state (e.g., email already in use) |
| 500         | Server Error | Unexpected server error                                           |

## Security Considerations

### Authentication and Authorization

- Session-based authentication using Flask-Login
- Role-based access control for different user types
- Secure password handling with proper hashing

### Data Protection

- Input validation on all endpoints
- Error messages designed to avoid leaking sensitive information
- File upload validation and restrictions

### CSRF Protection

For production use, CSRF protection is implemented to prevent cross-site request forgery attacks.

---

