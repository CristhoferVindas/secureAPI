# Secure API

A REST API built with Django REST Framework that provides user authentication and book management functionality. This API implements JWT authentication, rate limiting, and follows REST best practices.

## 🚀 Features

- **User Management:**
  - User registration and authentication
  - JWT token-based authentication
  - Rate limiting for API endpoints
  - Secure password handling

- **Book Management:**
  - CRUD operations for books
  - Protected endpoints requiring authentication
  - ISBN validation
  - Comprehensive book metadata management

## 🛠️ Prerequisites

- Python 3.8+
- Django 5.1+
- Django REST Framework
- SimpleJWT for Django REST Framework

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/secure-library-api.git
cd secure-library-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

## 📚 API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/register/` | Create a new user account |
| POST | `/users/token/` | Obtain JWT token pair |
| GET | `/users/protected/` | Test protected endpoint |

### Book Management Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | List all books |
| POST | `/books/` | Create a new book |
| GET | `/books/{id}/` | Retrieve a specific book |
| PUT | `/books/{id}/` | Update a specific book |
| DELETE | `/books/{id}/` | Delete a specific book |

## 🔒 Security Features

- Password hashing using Django's default PBKDF2 algorithm
- JWT token authentication
- Rate limiting (10 requests per minute per user)
- CSRF protection enabled
- Secure password validation rules

[Previous content remains the same until API Usage Examples section]

## 📖 API Usage Examples (Postman)

### User Registration
**Endpoint:** `POST http://localhost:8000/users/register/`
  
**Headers:**
```
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepass123"
}
```

### Obtaining JWT Token
**Endpoint:** `POST http://localhost:8000/users/token/`

**Headers:**
```
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "email": "john@example.com",
    "password": "securepass123"
}
```

**Response Example:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Creating a Book
**Endpoint:** `POST http://localhost:8000/books/`

**Headers:**
```
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "published_date": "2024-01-01",
    "isbn": "9781234567890",
    "description": "A comprehensive guide to Django"
}
```

### Get All Books
**Endpoint:** `GET http://localhost:8000/books/`

**Headers:**
```
Authorization: Bearer <your_access_token>
```

### Get Single Book
**Endpoint:** `GET http://localhost:8000/books/1/`

**Headers:**
```
Authorization: Bearer <your_access_token>
```

### Update Book
**Endpoint:** `PUT http://localhost:8000/books/1/`

**Headers:**
```
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "title": "Django for Beginners - Second Edition",
    "author": "William S. Vincent",
    "published_date": "2024-01-01",
    "isbn": "9781234567890",
    "description": "Updated guide to Django"
}
```

### Delete Book
**Endpoint:** `DELETE http://localhost:8000/books/1/`

**Headers:**
```
Authorization: Bearer <your_access_token>
```

> **Note**: Remember to replace `<your_access_token>` with the actual JWT token received from the token endpoint. In Postman, you can store this token as an environment variable for easier reuse.


## ✍️ Authors

* **Cristhofer Vindas ** - *Initial work* - [YourUsername](https://github.com/yourusername)

## 🙏 Acknowledgments

* Django REST Framework documentation
* SimpleJWT documentation
* Django documentation
