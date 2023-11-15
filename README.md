# PedalPro Backend

## The PedalPro project, a platform for organizing and joining bike rides

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

PedalPro is a platform that allows users to organize and participate in bike rides. The backend component is responsible for managing user data, rides, and related functionalities.

## Features

- User registration and authentication
- Ride creation and management
- User participation in rides
- Live ride tracking (TODO: If applicable)

## Setup

### Prerequisites

- Python (version 3.6 or higher)
- Flask
- PostgreSQL (or any other database supported by SQLAlchemy)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/stephenkiai/pedalpro-backend.git
   cd pedalpro-backend

   Install dependencies:    pip install -r requirements.txt
   Set up the database:     python manage.py db upgrade
   Create a .env file in the project root and configure your environment variables:
                            FLASK_APP=app.py
                            FLASK_ENV=development  #change to production when deploying
                            DATABASE_URI=postgresql://your-username:your-password@localhost:5432/your-database-name
                            JWT_SECRET_KEY=your-secret-key


    Run the Application:    flask run
The application will be available at http://localhost:5000.
```
### Usage

User Registration:

    Use the /register endpoint to create a new user account.
    Send a POST request with the user's name, email, password, and role.
    Example:

    curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "password": "password123", "role": "rider"}' http://localhost:5000/register

User Login:

    Use the /login endpoint to authenticate and obtain an access token.
    Send a POST request with the login identifier (email or name) and password.
    Example:

    curl -X POST -H "Content-Type: application/json" -d '{"login_identifier": "john@example.com", "password": "password123"}' http://localhost:5000/login

Create a Ride:

    Use the /ride/create endpoint to create a new ride.
    Send a POST request with ride details like name, location, distance, and start_datetime.
    Example:

    curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_ACCESS_TOKEN" -d '{"name": "Morning Ride", "location": "City Park", "distance": "10 km", "start_datetime": "2023-01-01 08:00:00"}' http://localhost:5000/ride/create

Join a Ride:

    Use the /ride/join/{ride_id} endpoint to join an existing ride.
    Send a POST request with the user_id.
    Example:

    curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_ACCESS_TOKEN" -d '{"user_id": "USER_ID_TO_JOIN"}' http://localhost:5000/ride/join/RIDE_ID_TO_JOIN

View Live Rides:

    Use the /ride/live endpoint to get a list of live rides.
    Send a GET request to retrieve live rides.
    Example:

curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://localhost:5000/ride/live


### API Documentation

User Registration (POST):

    Endpoint: /register
    Request:
        Method: POST
        Headers:
            Content-Type: application/json
        Body:

        json

    {
      "name": "John Doe",
      "email": "john@example.com",
      "password": "password123",
      "role": "rider"
    }

Response:

json

    {
      "message": "User registered successfully"
    }

User Login (POST):

    Endpoint: /login
    Request:
        Method: POST
        Headers:
            Content-Type: application/json
        Body:

        json

    {
      "login_identifier": "john@example.com",
      "password": "password123"
    }

Response:

json

    {
      "message": "Authentication successful",
      "access_token": "YOUR_ACCESS_TOKEN"
    }

Create a Ride (POST):

    Endpoint: /ride/create
    Request:
        Method: POST
        Headers:
            Content-Type: application/json
            Authorization: Bearer YOUR_ACCESS_TOKEN
        Body:

        json

    {
      "name": "Morning Ride",
      "location": "City Park",
      "distance": "10 km",
      "start_datetime": "2023-01-01 08:00:00"
    }

Response:

json

    {
      "message": "Ride created successfully",
      "ride_id": "NEW_RIDE_ID"
    }

Join a Ride (POST):

    Endpoint: /ride/join/{ride_id}
    Request:
        Method: POST
        Headers:
            Content-Type: application/json
            Authorization: Bearer YOUR_ACCESS_TOKEN
        Body:

        json

    {
      "user_id": "USER_ID_TO_JOIN"
    }

Response:

json

    {
      "message": "User joined the ride successfully"
    }

View Live Rides (GET):

    Endpoint: /ride/live
    Request:
        Method: GET
        Headers:
            Authorization: Bearer YOUR_ACCESS_TOKEN
    Response:

    json

[
  {
    "id": "LIVE_RIDE_ID",
    "name": "Morning Ride",
    "location": "City Park",
    "distance": "10 km",
    "start_datetime": "2023-01-01 08:00:00"
  },
  // More live rides...
]


### Contributing
We welcome contributions from the community! If you'd like to contribute to the PedalPro project, please follow these guidelines:

    Fork the repository on GitHub.
    Clone your forked repository (git clone https://github.com/stephenkiai/pedalpro-backend.git).
    Create a new branch for your feature or bug fix (git checkout -b feature/your-feature).
    Make your changes and commit them with descriptive messages.
    Push your changes to your forked repository (git push origin feature/your-feature).
    Create a pull request on the main repository.

