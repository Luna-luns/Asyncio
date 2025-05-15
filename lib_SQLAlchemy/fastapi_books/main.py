from database import engine
# from database import async_engine
from fastapi import FastAPI
from routers.books import router as books_router


app = FastAPI()
app.include_router(books_router, prefix="/books", tags=["books"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}

print(engine.connect())
# print(await async_engine.connect())