# Savannah Informatics - Backend Technical Challenge

This project is a simple Customers and Orders service built with Python, Django, and Django REST Framework.

## Features

-   Create and manage Customers.
-   Create and manage Orders associated with Customers. 
-   REST API for all operations.
-   Authentication via OpenID Connect (OIDC).
-   Sends an SMS alert via Africa's Talking when an order is created.
-   Unit tested with coverage reports. 
-   CI/CD pipeline using GitHub Actions. 
-   Containerized with Docker.

## Tech Stack

-   **Backend:** Python, Django, Django REST Framework
-   **Database:** PostgreSQL
-   **Authentication:** OpenID Connect
-   **Containerization:** Docker
-   **CI/CD:** GitHub Actions

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <repo-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    -   Copy the `.env.example` to `.env` and fill in your credentials.
    -   You will need a PostgreSQL database and credentials from an OIDC provider and Africa's Talking.

5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

-   `GET /api/customers/`: List all customers.
-   `POST /api/customers/`: Create a new customer.
-   `GET /api/orders/`: List all orders.
-   `POST /api/orders/`: Create a new order.

*All endpoints require OIDC authentication.*
