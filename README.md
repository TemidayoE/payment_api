# Payment API
A RESTful API built using Django to enable small businesses to accept payments via popular payment gateways like PayPal, Paystack, and Flutterwave. This API is designed to be simple, secure, and scalable for managing payment transactions with minimal customer information.

## Features
*__Payment Initialization__: Easily initialize payment requests via PayPal, Paystack, or Flutterwave.
* __Minimal Customer Info__: Store only the necessary customer information for processing payments.
* __Versioning__: API versioning to ensure compatibility with future updates.
* __CI/CD Pipeline__: Automated continuous integration and delivery to streamline deployment.
* __Testing__: Unit tests to ensure functionality and correctness of endpoints.
## Tech Stack
* __Backend__: Django (REST Framework)
* __Database__: PostgreSQL (or other relational databases)
* __Payment Gateways__: PayPal, Paystack, Flutterwave
* __Authentication__: JWT (JSON Web Tokens)
* __CI/CD__: GitHub Actions for automation
## Getting Started
## Prerequisites
* Python 3.10 or higher
* Django 4.x or higher
* SQLite3 (or other relational databases)
* pip (Python package installer)
* Virtual environment - pipenv (optional but recommended)

## Installation
1. Clone the repository:
```
git clone https://github.com/username/payment-api.git
```
2. Navigate to the project folder:
```
cd payment-api
```
3. Create and activate a virtual environment (optional):
```
python -m venv venv
source venv/bin/activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```

5. Set up environment variables:

Create a ".env" file in the root directory.
Add the necessary environment variables like API keys for PayPal, Paystack, and Flutterwave.
Example .env:
```
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_SECRET=your_paypal_secret
PAYSTACK_SECRET_KEY=your_paystack_secret_key
FLUTTERWAVE_SECRET_KEY=your_flutterwave_secret_key
DATABASE_URL=your_database_url
```

6. Run database migrations:
```
python manage.py migrate
```
7. Run the server:
```
python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/.

# API Endpoints
* POST /api/v1/payments/initialize-payment/: Initialize a payment with Paystack.
  * Request Body: Customer email, amount, payment method
  * Response: Payment initialization details and status.

*GET /api/v1/payments/verify-payment/<str: reference>: Verify the details and status with Paystack
  * Response: Verified payments details and status

# Running Tests

1. Run tests:
```
python manage.py test
```

2. This will execute all unit tests, including those for payment initialization and validation.

# CI/CD with GitHub Actions
This project uses GitHub Actions for CI/CD, ensuring that tests are automatically run on every push, and deployments are handled seamlessly.

## GitHub Actions Workflow
* The .github/workflows/ci-cd.yml file contains the CI/CD pipeline setup, which runs tests on push and pull request events.
* It deploys the project to the chosen hosting platform after a successful test run.

# Contributing
1. Fork the repository.
2. Create your branch (git checkout -b feature-name).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to your branch (git push origin feature-name).
5. Create a new Pull Request.
