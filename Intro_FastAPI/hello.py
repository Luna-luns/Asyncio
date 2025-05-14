from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def hello():
    """ path -> function(endpoint) """
    return "Hello, world!"


if __name__ == '__main__':
    uvicorn.run('hello:app', reload=True)