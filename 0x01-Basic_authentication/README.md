# Basic Authentication Project

## Introduction
This project focuses on implementing Basic Authentication on a simple API. Basic Authentication is a method for verifying the identity of users requesting access to a website or application. In this project, we will walk through each step of the authentication process to understand it thoroughly.

## Background Context
In the industry, it's recommended not to implement your own Basic Authentication system and instead use a module or framework that handles it for you, such as Flask-HTTPAuth in Python. However, for learning purposes, we will implement Basic Authentication from scratch to understand its underlying mechanisms.

## Learning Objectives
By completing this project, you will:

- Understand what authentication means in web development
- Learn about Base64 encoding and how it is used in authentication
- Implement Basic Authentication from scratch in a Python Flask application
- Gain familiarity with Flask and its features for handling authentication

## Project Structure
- The project consists of several tasks, each focusing on different aspects of Basic Authentication.
- Each task includes specific requirements and objectives to be achieved.
- Tasks involve setting up the server, implementing error handlers, creating authentication classes, and validating requests.

## Setup Instructions
To get started with the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip3 install -r requirements.txt`.
3. Start the server by running `API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app`.

## Tasks Overview
The project is divided into multiple tasks, each targeting a specific aspect of Basic Authentication. Here's a brief overview of the tasks:

- Task 0: Set up the basic API structure and start the server.
- Task 1: Implement an error handler for unauthorized requests (HTTP status code 401).
- Task 2: Implement an error handler for forbidden requests (HTTP status code 403).
- Task 3: Create an Auth class to manage API authentication.
- Task 4: Define routes that don't require authentication.
- Task 5: Validate all requests to secure the API.
- Task 6: Implement Basic Authentication by creating a BasicAuth class.
- Task 7: Extract the Base64 part of the Authorization header for Basic Authentication.
- Task 8: Decode the Base64 Authorization header for Basic Authentication.
- Task 9: Extract user credentials from the decoded Base64 Authorization header.
- Task 10: Retrieve the User object based on user credentials.
- Task 11: Overload the current_user method to retrieve User instance for requests.

## Usage
Once the server is running, you can test the API endpoints using tools like cURL or web browsers. Make requests to different endpoints to observe the authentication process and error handling.

## Advanced Tasks
The project also includes advanced tasks for further enhancement and exploration of Basic Authentication. These tasks cover topics such as allowing passwords with ":" and improving authentication requirement with wildcard paths.

## Contributor
- [Yohanes Senbeto](https://github.com/YohanesSenbeto) - Project Lead

## Acknowledgments
Special thanks to the ALX School community for providing guidance and resources for this project
