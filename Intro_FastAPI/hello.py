from fastapi import FastAPI
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


if __name__ == '__main__':
    uvicorn.run('hello:app', reload=True)