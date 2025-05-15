from fastapi import Body, FastAPI, HTTPException
import uvicorn

import booksDB
from models.book import Book, SBookRequest, SBookResponse


app = FastAPI()


@app.get("/books", summary="Получить все книги")
def get_books() -> list[SBookResponse]:
    return booksDB.data


@app.get("/books/{book_id}", summary="Получить книгу по id", response_model=SBookResponse)
def get_book_byid(book_id: int) :
    for book in booksDB.data:
        if book["id"] == book_id:
            return book
    raise HTTPException(404, f"Book with id={book_id} not Found")


@app.post("/books", summary="Добавить новую книгу")
def create_book(book: Book = Body(embed=True)) -> SBookResponse:
    temp = {
        "id": len(booksDB.data) + 1,
        "title": book.title,
        "text": book.text,
        "author": book.author
        }
    booksDB.data.append(temp)
    return temp



@app.put("/books/{book_id}", summary="Изменить книгу по id")
def edit_book_byid(book_id: int, book: SBookRequest = Body(embed=True)) -> SBookResponse | dict:
    book = book.model_dump(exclude_none=True) 
    if book:
        for index, cur_book in enumerate(booksDB.data):
            if cur_book["id"] == book_id:
                booksDB.data[index].update(book)
                return booksDB.data[index]
        raise HTTPException(404, f"Book with id={book_id} not Found")
    raise HTTPException(400, "Bad Request")


@app.delete("/books/{book_id}", summary="Удалить книгу по id")
def delete_book_byid(book_id: int) -> dict:
    for index, book in enumerate(booksDB.data):
        if book["id"] == book_id:
            booksDB.data.pop(index)
            return {"message": "Book deleted successfully"}
    return {"status": 404, "message": "Not Found"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
