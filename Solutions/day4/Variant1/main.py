from fastapi import Body, FastAPI, Response
from pydantic import BaseModel
import uvicorn
import asyncio
import json

books_db = {}

error_dict = {"detail": "Book not found"}
success_dict = {"message": "Book deleted successfully"}

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str | None = None

@app.post('/books')
async def create_book(book: Book):
    new_id = len(books_db) + 1
    books_db[new_id] = book
    book_json = {"book_id": new_id,"book": book}
    return book_json

@app.get('/books')
async def read_books():
    return books_db

@app.get('/books/{book_id}')
async def read_book_by_id(book_id: int):
    if books_db.get(book_id):
        return books_db[book_id]
    return Response(content=json.dumps(error_dict), media_type="text/plain", status_code=404)
     

@app.put('/books/{book_id}')
async def update_books(book: Book, book_id: int):
    new_book = book.model_dump(exclude_none=True, exclude_unset=True)
    if books_db.get(book_id):
        for key, value in new_book.items():
            setattr(books_db[book_id], key, value)
        book_json = {"book_id": book_id,"book": books_db[book_id]}
        return book_json
    return Response(content=json.dumps(error_dict), media_type="text/plain", status_code=404)

@app.delete('/books/{book_id}')
async def delete_books(book_id: int):
    if books_db.get(book_id):
        del books_db[book_id]
        return success_dict
    return Response(content=json.dumps(error_dict), status_code=404)


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)