# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a simple REST API using FastAPI. You will learn how to define endpoints, validate request data, and return structured JSON responses for common create, read, update, and delete operations.

## 📝 Tasks

### 🛠️ Build Core API Endpoints

#### Description
Create a FastAPI application for managing a small collection of books. Implement endpoints that allow users to view and add books using JSON data.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Implement `GET /books` to return all books as a JSON list.
- Implement `POST /books` to add a new book using request body data.
- Return appropriate HTTP status codes (for example, `200` for successful reads and `201` for successful creation).


### 🛠️ Add Validation and Item Lookup

#### Description
Enhance the API with validation and item-level operations so users can retrieve, update, and delete individual books by ID.

#### Requirements
Completed program should:

- Use a Pydantic model to validate incoming book data (`title`, `author`, and `year`).
- Implement `GET /books/{book_id}` to return a single book or a `404` error if not found.
- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book and return a clear success response.
- Provide clear error messages for invalid input and missing records.
