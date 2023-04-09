# Scraping Twitter User API

## Introduction

Selenium Driver Client is a FastAPI-based application designed to scraping media from twitter's user using Selenium and Undetected-Chromedriver. The application provides endpoints to interact with a headless Chrome browser and retrieve photos from the user designed or random . This tool can be useful for web scraping, testing, and automation tasks.

## API Endpoints

This section describes the available API endpoint.

### Rendering Endpoint

**URL**: `/scrap`

**Method**: `POST`

**Input**: UserCredentials(contains the URL to be rendered, API key for authentication and tbe proxy provider id)

**Output**: Photos from the user scraped

**Description**: This endpoint scrap a twitter user using selenium and undetected_chromedriver, then returns the photos inside a folder called ''chocolatito'. It first validates the provided API key. If the validation fails, it raises an HTTP exception with a 401 status code and an "Unauthorized" detail. If the validation is successful, it initializes the Chrome driver with the appropriate options and loads the requested URL. It then retrieves the page source, current URL, and cookies. After closing and quitting the driver, it prepares the response content and returns a JSON response with a 200 status code.

## Getting Started

The following section provides instructions for setting up and running the application locally and with Docker. Prior to running the application, ensure that you have met the prerequisites, installed the necessary dependencies, and properly configured the environment variables. Follow the step-by-step instructions below to get started.

### Prerequisites

- Python 3.10 or higher
- Docker installed

### Installation

1. Clone the repository
2. Set up a virtual environment (optional)
3. Install dependencies

### Running the application

#### Running locally

Use uvicorn to run the application with the following configurations:

- Reloads the app when there is any change in the code, disable this flag in the production environment.
- Sets the application to run on port 80. Ensure the port is free or change the port accordingly.

```bash
    uvicorn main:app --reload --port 80
```

#### Running with Docker

To deploy the application using Docker, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your system.
2. Build the Docker image by running the following command in the project root directory:

```bash
    docker-compose build
```

3. Start the Docker container using Docker Compose:

```bash
    docker-compose up
```

The application will be running on port 80 by default. You can access the API by navigating to http://localhost in your browser or any API client.

To stop the Docker container, press Ctrl+C or run the following command in another terminal window:

```bash
    docker-compose down
```

# API Documentation

The API documentation provides detailed information on the endpoints available in the application, the expected request parameters and response objects, as well as any additional information related to the usage of the API.

## Swagger UI

The API documentation can be accessed through the Swagger UI interface. To access it, simply navigate to http://localhost:80/docs in your browser.

The Swagger UI provides a user-friendly interface to interact with the API, allowing users to test the endpoints, view example requests and responses, and explore the available parameters.

## Redoc

Alternatively, the documentation can be accessed through the Redoc interface by navigating to http://localhost:80/redoc in your browser. Redoc provides a clean, easy-to-read interface for the API documentation, allowing users to quickly and easily understand the API's capabilities and usage.

Both Swagger UI and Redoc are automatically generated based on the OpenAPI (formerly Swagger) specification, which is maintained alongside the application code. This ensures that the API documentation is always up-to-date and accurately reflects the API's capabilities.
