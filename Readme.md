
# 🏆 Event Management API

A **Django REST Framework** (DRF)-based API for managing events. This project allows users to register, create and manage events, sign up for events, and receive email notifications upon successful registration. It also includes **Docker support** for an easy deployment experience.

---

## 📌 Table of Contents

- [🚀 Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [📋 Prerequisites](#-prerequisites)
- [📍 Local Setup](#-local-setup)
  - [🔧 Installation](#-installation)
  - [🌍 Environment Variables](#-environment-variables)
  - [💾 Database Setup](#-database-setup)
  - [🛠 Running Migrations](#-running-migrations)
  - [🚀 Starting the Development Server](#-starting-the-development-server)
- [📝 API Endpoints](#-api-endpoints)
- [📄 API Documentation](#-api-documentation)
- [📧 Email Notifications](#-email-notifications)
- [🔒 Security & Best Practices](#-security--best-practices)
- [📜 License](#-license)

---

## 🚀 Features

- **User Registration & Token Authentication**: Secure user registration and authentication.
- **Event Management (CRUD)**: Users can create, read, update, and delete events.
- **Event Registration**: Users can sign up for events.
- **Email Notifications**: Users receive an email when they successfully register for an event.
- **Advanced Filtering**: Search for events by title, date range, or organizer’s username.
- **Docker Support**: Easily deployable using Docker and Docker Compose.
- **Interactive API Documentation**: Built-in Swagger and Redoc support for better API exploration.

---

## 🛠 Tech Stack

- **Backend**: Python 3.10+, Django, Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **API Documentation**: drf-yasg (Swagger/Redoc)
- **Email Sending**: SMTP support (e.g., Gmail, SendGrid)
- **Filtering**: django-filter

---

## 📋 Prerequisites

- **Python 3.10+**
- **pip** (Python package manager)
- **Git**
- **PostgreSQL**
- **Docker & Docker Compose**

---

## 📍 Local Setup

### 🔧 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/l1stopad/event_managament
   cd event-management
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   ```

   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

### 🌍 Environment Variables

Create a `.env` file in the project root and add the following:

```ini
# .env

# Django settings
SECRET_KEY=your_super_secret_key
DEBUG=True

# Database configuration
DB_NAME=event_db
DB_USER=postgres
DB_PASSWORD=postgres_password
DB_HOST=localhost
DB_PORT=5432

# Email configuration
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
```

> **⚠️ Important:** Add `.env` to `.gitignore` to prevent it from being pushed to version control.

---

### 💾 Database Setup

Ensure PostgreSQL is installed and running. You can also use SQLite for quick local testing.

---

### 🛠 Running Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🚀 Starting the Development Server

```bash
python manage.py runserver
```

Your API is now accessible at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

To create a **superuser** (admin):

```bash
python manage.py createsuperuser
```


### 🏗 Running the Project with Docker

#### 🛠 **Step 1: Create the `.env` file**
Make sure you have a `.env` file in the project root with **database credentials**:

```ini
# .env

# Django settings
SECRET_KEY=your_super_secret_key
DEBUG=True

# Database configuration
DB_NAME=event_db
DB_USER=postgres
DB_PASSWORD=postgres_password
DB_HOST=db
DB_PORT=5432

# Email settings
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
```

> **IMPORTANT**:  
> The `DB_HOST` should be set to `db` instead of `localhost`, because the **web service** will connect to the **database service** within the **Docker network**.

---

#### 🛠 **Step 2: Build and Start the Containers**
Run the following command to build the containers and start the services:

```bash
docker-compose up --build
```

To **run in detached mode** (in the background), use:

```bash
docker-compose up -d --build
```

---

#### 🛠 **Step 3: Apply Migrations**
Once the containers are running, apply database migrations:

```bash
docker-compose exec web python manage.py migrate
```

---

#### 🛠 **Step 4: Create a Superuser (Optional)**
To create an admin user:

```bash
docker-compose exec web python manage.py createsuperuser
```

---

#### 🛠 **Step 5: Check Running Containers**
To see the running Docker containers:

```bash
docker ps
```

---

#### 🛠 **Step 6: Stop the Containers**
To gracefully stop the containers:

```bash
docker-compose down
```

---

#### 🛠 **Step 7: Restart the Containers**
To restart after making changes:

```bash
docker-compose restart
```

---

### 🚀 **Accessing the Application**
Once the containers are up and running:

- **API is available at**:  
  🖥 `http://127.0.0.1:8000/`

- **Django Admin Panel** (after creating a superuser):  
  🔑 `http://127.0.0.1:8000/admin/`

- **Swagger API Documentation**:  
  📑 `http://127.0.0.1:8000/swagger/`

- **Redoc API Documentation**:  
  📖 `http://127.0.0.1:8000/redoc/`

---


## 📝 API Endpoints

| Method | Endpoint                        | Description |
|--------|---------------------------------|-------------|
| `POST` | `/api/register/`                | User registration |
| `POST` | `/api-token-auth/`              | Get authentication token |
| `GET`  | `/api/events/`                  | List events |
| `POST` | `/api/events/`                  | Create event |
| `GET`  | `/api/events/{id}/`             | Retrieve event |
| `PUT`  | `/api/events/{id}/`             | Update event |
| `DELETE` | `/api/events/{id}/`           | Delete event |
| `POST` | `/api/events/{id}/register/`    | Register for an event |
| `GET`  | `/api/my-registrations/`        | Get registered events |

---

## 📄 API Documentation

Swagger and Redoc documentation is available:

- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

To authorize in Swagger, click **“Authorize”** and enter your token as:

```
Token <your_token>
```

---

## 📧 Email Notifications

Emails are sent when a user registers for an event. To configure email sending:

1. **Use SMTP settings in `.env`**:
   ```ini
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```
2. **For development, print emails in the console**:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   ```

---

## 🔒 Security & Best Practices

- **Never commit `.env` files** with sensitive data.
- **Use `DEBUG=False`** in production.
- **Consider a reverse proxy like Nginx** for handling requests in production.
- **Use Gunicorn** instead of Django’s built-in server for better performance.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

🚀 **Thank you for using Event Management API!**  
For contributions, feedback, or issues, please open an issue or submit a pull request.

---