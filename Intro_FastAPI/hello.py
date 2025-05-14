import asyncio
from fastapi import Body, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def hello():
    """ path -> function(endpoint) """
    return "Hello, world!"

@app.get('/hello/{who}')
def hello_who(who: str):
    """ Пример динамического URL'a. """
    return f'Hello, {who}!'


@app.get('/hello')
def hello_query(who: str):
    """ Пример использования query parameters 
        URL example: /hello?who=Mark
    """
    return f'Hi, {who}!'


@app.post('/hello')
def body_name(who = Body(embed=True)):
    user_names = []
    user_names.append(who)
    if who != "Petr":
        raise HTTPException(status_code=404, detail=f"Bad user's name: {who}")
    content = {"message": f'Hello, {who}!'}
    headers = {"Status-Code": "404", "X-My-name": "value"}
    return JSONResponse(content=content, headers=headers)


class User(BaseModel):
    # Обязательное поле 'name' типа строка
    name: str
    # Необязательное поле 'age' (может быть None или строкой)
    age: int | None = None


@app.post('/user')
def create_user(user: User) -> str:
    print(f'Out: {type(user)}')
    return f'Hello, {user.name}. You are {user.age or 0} years old.'


@app.get("/async_hello")
async def get_async_url():
    """Async function example. """
    await asyncio.sleep(1)
    return f'Done.'



if __name__ == '__main__':
    uvicorn.run('hello:app', reload=True)