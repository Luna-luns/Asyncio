from pydantic import BaseModel


class Book(BaseModel):
    title: str
    text: str
    author: str

class SBookRequest(Book):
    title: str | None = None
    text: str | None = None
    author: str | None = None


class SBookResponse(Book):
    id: int
