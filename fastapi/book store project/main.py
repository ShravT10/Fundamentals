from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Book(BaseModel):
    title: str
    author: str
    publication_year: int
    isbn: int

Books = []

app = FastAPI(title="Book Store")

@app.post('/add-book')
async def add_book(book: Book):
    Books.append(book)
    return {"Message":f"Book {book.title} successfully added to the store"}

@app.get('/show-books')
async def show_books():
    return Books

@app.get('/get-book/{isbn}')
async def get_a_book(isbn: int):
    book = [s.title for s in Books if s.isbn == isbn] or None

    if book is None:
        return {"Message":f"No book with isbn {isbn}"}
    
    return {"Message":f"Book with isbn {isbn} is {book}"}
            
@app.delete('/del-book/{isbn}')
async def del_a_book(isbn: int):
    book = next((s for s in Books if s.isbn == isbn), None)

    if book is None:
        return {"Message":f"No book with isbn {isbn}"}
    
    Books.remove(book)
    return {"Message":f"Book {book.title} Deleted"}
