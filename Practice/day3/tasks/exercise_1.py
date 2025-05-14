import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def say_hello() -> str:
    return 'Hello, World!'


if __name__ == '__main__':
    uvicorn.run(reload=True, app='exercise_1:app')
