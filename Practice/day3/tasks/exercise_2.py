import uvicorn
from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str | None = None
    year: int | None = None
    genre: str | None = None


books: dict = {
    1: Book(id=1, title='Три мушкетера', author='Александр Дюма', year=1844, genre='Приключенческий роман'),
    2: Book(id=2, title='Повелитель мух', author='Уильям Голдинг', year=1954, genre='роман'),
    3: Book(id=3, title='Горе от ума', author='Александр Сергеевич Грибоедов', year=1825, genre='комедия')
}


@app.get('/books')
def get_books() -> list:
    """Returns book list."""
    return list(books.values())


@app.get('/books/{book_id}')
def get_book_id(book_id: int):
    """Returns book by id."""
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]


@app.post('/books')
def create_book(title: str = Body(embed=True), author: str | None = Body(embed=True)) -> tuple:
    """Creates new book."""
    new_id = max(books.keys()) + 1 if books else 1
    new_book = Book(id=new_id, title=title, author=author)
    books[new_id] = new_book
    return new_id, new_book


@app.put('/books/{book_id}')
def update_book(book_id: int, title: str = Body(embed=True), author: str | None = Body(embed=True)) -> dict:
    """Updates book info."""
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    book = books[book_id]
    book.title = title
    book.author = author
    return {"message": f"Book with id {book_id} updated"}


@app.delete('/books/{book_id}')
def delete_book(book_id: int) -> dict:
    """Deletes book."""
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]
    return {"message": f"Book with id {book_id} deleted"}


if __name__ == '__main__':
    uvicorn.run(reload=True, app='exercise_2:app')
