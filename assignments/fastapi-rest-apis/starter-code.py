from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    author: str = Field(min_length=1, max_length=80)
    year: int = Field(ge=0, le=2100)


class Book(BookCreate):
    id: int


books: List[Book] = [
    Book(id=1, title="The Pragmatic Programmer", author="Andrew Hunt", year=1999),
    Book(id=2, title="Clean Code", author="Robert C. Martin", year=2008),
]


@app.get("/books", response_model=List[Book])
def get_books() -> List[Book]:
    return books


@app.post("/books", response_model=Book, status_code=201)
def create_book(payload: BookCreate) -> Book:
    new_id = max([book.id for book in books], default=0) + 1
    new_book = Book(id=new_id, **payload.model_dump())
    books.append(new_book)
    return new_book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, payload: BookCreate) -> Book:
    for index, book in enumerate(books):
        if book.id == book_id:
            updated = Book(id=book_id, **payload.model_dump())
            books[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict:
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"message": f"Book {book_id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
