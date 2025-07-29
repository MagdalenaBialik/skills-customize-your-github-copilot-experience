from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# In-memory storage for books
books_db: List[Book] = []

# TODO: Implement API endpoints for CRUD operations
# - GET /books
# - GET /books/{id}
# - POST /books
# - PUT /books/{id}
# - DELETE /books/{id}
