# Fetch-Receipt-processor

A Flask-based web service that processes and scores receipts based on specified rules. This application provides endpoints to submit receipts, calculate and retrieve points for each receipt.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
  - [POST /receipts/process](#post-receiptsprocess)
  - [GET /receipts/{id}/points](#get-receiptsidpoints)
- [Points Calculation Rules](#points-calculation-rules)
- [Testing](#testing)
- [Development Notes](#development-notes)

---

## Project Overview

The Receipt Processor is a microservice that:
1. Accepts a JSON payload containing receipt data.
2. Calculates points based on predefined rules.
3. Returns an ID for the receipt.
4. Allows retrieval of the points awarded using the ID.

In-memory storage is used, meaning data does not persist when the application stops.

## Features
- Receipt processing with unique ID generation.
- Point calculation based on various rules.
- Retrieval of receipt points via ID.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd receipt-processor
    ```

2. Install dependencies using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Docker Setup

1. Build the Docker image:
    ```bash
    docker build -t receipt-processor .
    ```

2. Run the container:
    ```bash
    docker run -p 5000:5000 receipt-processor
    ```

## Running the Application

After setting up the application, you can access it on `http://localhost:5000`.

## API Documentation

### POST /receipts/process

- **Description**: Accepts a receipt JSON object and calculates the points based on defined rules.
- **Path**: `/receipts/process`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "retailer": "RetailerName",
      "purchaseDate": "YYYY-MM-DD",
      "purchaseTime": "HH:MM",
      "items": [
        {
          "shortDescription": "Item Description",
          "price": "12.34"
        }
      ],
      "total": "56.78"
    }
    ```
- **Response**:
    ```json
    { "id": "unique-receipt-id" }
    ```

- **Example**:
    ```json
    { "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
    ```

### GET /receipts/{id}/points

- **Description**: Retrieves the points awarded for a processed receipt.
- **Path**: `/receipts/{id}/points`
- **Method**: `GET`
- **Response**:
    ```json
    { "points": 32 }
    ```

- **Example**:
    ```json
    { "points": 109 }
    ```

## Points Calculation Rules

Points are awarded based on the following rules:

1. **Retailer Name**: 1 point for every alphanumeric character.
2. **Total**:
    - 50 points if it's a round dollar amount (no cents).
    - 25 points if it’s a multiple of 0.25.
3. **Items**:
    - 5 points for every two items.
    - If the item’s description length (trimmed) is a multiple of 3, multiply the price by 0.2, round up, and add to the points.
4. **Purchase Date**: 6 points if the day is odd.
5. **Purchase Time**: 10 points if between 2:00 PM and 4:00 PM.

## Testing

Tests are written using `pytest` and `pytest-flask`. To run tests:

1. Install the test dependencies if they aren’t already installed:
    ```bash
    pip install pytest pytest-flask
    ```

2. Run the tests:
    ```bash
    pytest
    ```

## Development Notes

- **Project Structure**:
  - `app.py`: Main entry point for the Flask application.
  - `endpoints/`: Contains separate files for each endpoint (e.g., `process_receipt.py`, `get_points.py`).
  - `utils/`: Contains utility functions for point calculation, broken down by rule.
  - `tests/`: Contains test cases for endpoints and utility functions.

- **Configuration**:
  - Modify configurations in `config.py` if additional settings are required in the future.

- **Docker**:
  - The application is containerized. To start fresh, stop any existing containers with:
    ```bash
    docker ps
    docker stop <container_id>
    ```

---

This README serves as both a guide and documentation to run, test, and develop on the Receipt Processor project. Happy coding!
