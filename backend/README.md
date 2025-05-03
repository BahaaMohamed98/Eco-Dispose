# Eco-Dispose Backend

Flask API server providing user authentication, device tracking, and file uploads.

## Technology Stack

- **Framework**: Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Password Security**: Werkzeug's password hashing
- **API**: RESTful architecture

## Architecture

The backend follows a modular structure with:

- Flask blueprints for route organization
- SQLAlchemy ORM for database interactions
- JWT authentication for secure API access

## project structure

```text
backend/
├── app/
│   ├── __init__.py      # Flask app initialization
│   ├── auth.py          # Authentication routes
│   ├── config.py        # Configuration settings
│   ├── devices.py       # Device management routes
│   ├── models.py        # Database models
│   └── util.py         # Helper functions
├── .env.example         # Environment variables template
└── requirements.txt     # Python dependencies
```

## Setup

### Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Configure environment variables

Copy `.env.example` to `.env` and set the required environment variables:

```bash
# Copy example environment file to .env
cp .env.example .env # Windows: copy .env.example .env
```

Edit the `.env` file to set your environment variables:

- `SECRET_KEY`: Secret key for session management and CSRF protection.
- `SQLALCHEMY_DATABASE_URI`: Database connection for SQLite.

Generate a secure random SECRET_KEY with:

```bash
python -c 'import secrets; print(secrets.token_hex())'
```

The application reads these configuration values for security and database connections.

### Run development server

```bash
flask run --debug
```

## API Endpoints

### [Authentication](../docs/api/auth.md)

- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/profile` - Get user profile
- `POST /auth/edit` - Update user profile
- `POST /auth/logout` - User logout

### [Devices](../docs/api/devices.md)

- `GET /devices` - List user's devices
- `POST /devices` - Submit new device
- `PUT /devices/<id>` - Update device status
- `DELETE /devices/<id>` - Delete device

## [Database Models](../docs/api/index.md#database-schema)

- `User` - User accounts with authentication details
- `Device` - Electronic devices submitted for recycling
- `Address` - User address information

## Error Handling

The API uses standard HTTP status codes for error handling. Common errors include:

- `200 OK` - Successful request
- `400 Bad Request` - Invalid input data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Access denied
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error
