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


### API Documentation



