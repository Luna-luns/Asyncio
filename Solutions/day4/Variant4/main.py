import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str | None = None

class BookResp(Book):
    id: int


# Класс хранилище
class Book_storage():
    def __init__(self):
        self.id = 0
        self.storage = {}

    async def add_book(self, book: Book) -> BookResp:
        self.id += 1
        self.storage[self.id] = {'title': book.title,
                                 'author': book.author}
        await asyncio.sleep(0.5)
        return BookResp(**(self.storage[self.id] | {"id": self.id}))


    async def get_book_by_id(self, index: int):
        await asyncio.sleep(0.5)
        return self.storage[index]

    async def get_books(self):
        await asyncio.sleep(0.5)
        return self.storage

    async def put_book(self, index: int, book: Book):
        update_book = book.model_dump(exclude_unset=True, exclude_none=True)

        if index in self.storage:
            self.storage[index].update(update_book)
            return self.storage[index]
        raise KeyError


    async def delete_book(self, index: int):
        await asyncio.sleep(0.5)
        del self.storage[index]


bookStorage = Book_storage()


@app.post('/books')
async def post_book(book: Book):
    return await bookStorage.add_book(book)


@app.get('/books')
async def get_books() -> JSONResponse:
    return JSONResponse(content=await bookStorage.get_books())


@app.get('/books/{book_id}')
async def get_book(book_id: int) -> JSONResponse:
    try:
        return JSONResponse(content=await bookStorage.get_book_by_id(book_id))
    except KeyError:
        raise HTTPException(status_code=404,
                            detail={"error": "Данный id не найден"})


@app.put('/books/{book_id}')
async def put_book(book: Book, book_id: int):
    try:
        result = await bookStorage.put_book(book_id, book)

        return result
    except KeyError:
        raise HTTPException(status_code=404,
                            detail={"error": "Данный id не найден"})


@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    try:
        await bookStorage.delete_book(book_id)
        return {"message": f"Книга с id={book_id} удалена"}
    except KeyError:
        raise HTTPException(status_code=404, detail={"error": "Данный id не найден"})


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
