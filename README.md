# django-token-login
# Django JWT Authentication and User Profile Example

This repository provides an example implementation of user registration, login, and user profile functionality using Django framework and JSON Web Tokens (JWT) for authentication. It's designed to help you understand and kickstart your development process when building user authentication and profile features in your Django applications.

## Features

- User registration with email and password
- User login with JWT-based authentication
- User profile management
- Token-based authentication for secure API endpoints
- Django Admin panel integration for user management
- -implemented with postgres database


## Usage

1. Register a new user using the registration endpoint (`/api/register/`).
2. Log in with the registered user credentials using the login endpoint (`/api/login/`).
3. Access protected API endpoints by including the JWT token in the request headers:

   ```http
   Authorization: Bearer your_token_here
   ```


## Configuration

- JWT secret key and expiration settings can be configured in the `settings.py` file.
- You can customize the user profile model and fields according to your requirements.

## Contributing

Contributions to this project are welcome! If you find a bug or want to add a new feature, please create an issue or submit a pull request.
