# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. You will practice creating endpoints, handling requests and responses, and working with data models.

## 📝 Tasks

### 🛠️ Create a Simple REST API

#### Description
Build a FastAPI application that exposes a REST API for managing a collection of books. Each book should have an ID, title, author, and publication year. Implement endpoints to list all books, retrieve a single book by ID, add a new book, update an existing book, and delete a book.

#### Requirements
Completed program should:
- Use FastAPI to define API endpoints
- Support GET (list all books, get by ID), POST (add), PUT (update), and DELETE (remove)
- Use Pydantic models for request and response validation
- Store data in memory (a Python list or dictionary)
- Return appropriate HTTP status codes and error messages

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API to validate input data and handle errors gracefully (e.g., book not found, invalid data).

#### Requirements
Completed program should:
- Validate that all required fields are present and correct
- Return 404 for missing books, 400 for invalid input
- Provide clear error messages in JSON format

