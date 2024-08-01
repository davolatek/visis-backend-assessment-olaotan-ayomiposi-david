Book Summary API
This project provides an API to manage book information and generate summaries using an AI model. The API is built using FastAPI, and MongoDB is used as the database to store book data.

Features
Add, update, and retrieve book information.
Generate and retrieve summaries for books based on their descriptions.
Prerequisites
To set up and run this project, you need the following:

Python 3.8+
MongoDB Atlas account (or a local MongoDB instance)
FastAPI
Uvicorn
Setup
Clone the Repository
git clone <repository-url>
cd book_summary_api

### Set Up Local environement

It is recommended you create a virtual environment, to do that, use, python -m venv venv
Activate the virtual environment by running one of the following command:
On windows: venv\Scripts\activate
On MacOS/Linux: source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### To run the application

uvicorn main:app --reload

### API Documentation

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

### Video Demonstration Link

https://youtu.be/AC1cJxsbLus
