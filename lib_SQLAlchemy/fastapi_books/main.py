# from database import engine
from database import async_engine

# print(engine.connect())
print(await async_engine.connect())