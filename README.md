# Flight Services

![License](https://img.shields.io/github/license/Macgyver02/Flight-services)
![Version](https://img.shields.io/github/package-json/v/Macgyver02/Flight-services)
![Build Status](https://img.shields.io/github/actions/workflow/status/Macgyver02/Flight-services/ci.yml)
![Issues](https://img.shields.io/github/issues/Macgyver02/Flight-services)
![Contributors](https://img.shields.io/github/contributors/Macgyver02/Flight-services)
![Last Commit](https://img.shields.io/github/last-commit/Macgyver02/Flight-services)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
  - [Authentication](#authentication)
  - [Endpoints](#endpoints)
  - [Error Handling](#error-handling)
- [Testing](#testing)
- [CI/CD Integration](#cicd-integration)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

## Introduction

Flight Services is a scalable, microservices-based flight booking system designed for airlines, travel agencies, and third-party travel platforms. It provides core functionalities like searching for flights, booking, cancellations, and payment processing.

This system is built with reliability, performance, and scalability in mind to ensure seamless transactions and management of large datasets.

## Features

- **Search for Flights:** Easily search for available flights based on criteria such as destination, date, and price.
- **Real-Time Booking:** Book tickets in real time, including seat selection and baggage options.
- **Flight Status Notifications:** Receive real-time updates on flight schedules and delays.
- **Cancellation and Refund:** Manage ticket cancellations and refunds with ease.
- **Multi-Currency Payment:** Support for multiple currencies and payment methods.
- **Admin Dashboard:** A role-based admin panel to manage flight schedules, bookings, and payments.

## Tech Stack

**Backend:**

- **Node.js** (Runtime)
- **Express.js** (Web framework)
- **MongoDB** (Database)
- **Redis** (Caching)
- **RabbitMQ** (Message queue for handling async tasks)
- **RESTful API** (for external communication)
  
**Frontend:**

- **React.js** (User Interface)
- **Redux** (State Management)
- **Tailwind CSS** (UI Styling)

**DevOps:**

- **Docker** (Containerization)
- **Kubernetes** (Container Orchestration)
- **Jenkins** (CI/CD)
- **AWS** (Cloud infrastructure, including EC2, S3, and RDS)
  
## Architecture

Flight Services is designed with a microservices architecture to ensure high scalability and fault tolerance. Each service handles a specific responsibility, and they communicate via HTTP/REST or through a message broker (RabbitMQ).

- **User Service:** Handles user authentication, registration, and management.
- **Flight Service:** Manages flight schedules, real-time availability, and inventory.
- **Booking Service:** Manages user bookings, seat selection, and cancellations.
- **Payment Service:** Handles payments, including third-party integration for multi-currency support.
- **Notification Service:** Sends flight status notifications and booking confirmations via email/SMS.

![System Architecture](https://github.com/Macgyver02/Flight-services/docs/architecture.png)

## Installation

### Prerequisites

- **Node.js** (v14.x or higher)
- **MongoDB** (v4.x or higher)
- **Redis** (optional for caching)
- **RabbitMQ** (optional for async tasks)
- **Docker** (optional for containerization)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Macgyver02/Flight-services.git
    cd Flight-services
    ```

2. **Install dependencies:**

    ```bash
    npm install
    ```

3. **Run MongoDB locally** (or configure to connect to a cloud instance):

    ```bash
    mongod --port 27017
    ```

4. **Start the development server:**

    ```bash
    npm start
    ```

## Configuration

The project requires configuration of environment variables. Create a `.env` file in the root directory with the following:

```bash
PORT=3000
MONGO_URI=mongodb://localhost:27017/flight-services
JWT_SECRET=<your-jwt-secret>
REDIS_URL=redis://localhost:6379
RABBITMQ_URL=amqp://localhost
PAYMENT_API_KEY=<your-payment-gateway-api-key>
```

## API Documentation

All endpoints are versioned under `/api/v1`. Below is a brief overview of the main routes.

### Authentication

- **POST /api/v1/auth/login:** User login and JWT token issuance.
- **POST /api/v1/auth/register:** User registration.

### Endpoints

- **GET /api/v1/flights/search:** Search for available flights.
- **POST /api/v1/bookings:** Book a flight.
- **POST /api/v1/bookings/cancel:** Cancel an existing booking.
- **GET /api/v1/flights/status/:flightId:** Check the status of a flight.

### Error Handling

Standard error response structure:

```json
{
  "error": true,
  "message": "Resource not found",
  "statusCode": 404
}
```

Errors are categorized based on HTTP status codes: 4xx for client-side errors, and 5xx for server-side errors.

## Testing

We use **Jest** and **Supertest** for unit and integration testing.

1. **Run unit tests:**

    ```bash
    npm test
    ```

2. **Run integration tests:**

    ```bash
    npm run test:integration
    ```

Testing includes coverage for all API endpoints and business logic. The goal is 90%+ coverage across the application.

## CI/CD Integration
