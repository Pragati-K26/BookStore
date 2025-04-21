# 📚 Bookstore Management System

A web-based Bookstore Management System built with Django. It supports user authentication, book listing, cart management, and admin controls. The project is containerized using Docker and 
integrated with Jenkins for CI/CD.


## 🚀 Project Overview

This system allows users to:
- Sign up, log in, and log out
- Browse books
- Add books to a cart
- View and manage the cart

Admins can:
- Add, update, and delete books via the Django admin panel

## 🛠️ Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (manual templates)
- **Database**: SQLite (default Django DB)
- **DevOps**: Docker, Docker Compose, Jenkins
- **Others**: Git, GitHub

🐳 Docker
Docker is used to containerize the Django Bookstore application to ensure consistency across different environments.

Key Benefits:
Simplifies setup with no need to install Python/Django manually

Easy deployment with docker-compose

Isolated development environment

Docker Setup Includes:
Dockerfile: Builds the Django app container

docker-compose.yml: Manages the app container and any supporting services (like databases, if added in future)

🤖 Jenkins
Jenkins automates the process of building, testing, and deploying the Django project.

Jenkins is used to:
Pull the latest code from GitHub

Build the Docker image

Run the application in a Docker container

Enable CI/CD (Continuous Integration and Deployment)
