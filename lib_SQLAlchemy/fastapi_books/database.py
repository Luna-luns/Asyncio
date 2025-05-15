from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, declarative_base, Session
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
    
# DATABASE_URL_ASYNC = "sqlite+aiosqlite:///./a_books.db"
# DATABASE_URL = "sqlite:///./books.db"
#
# # engine = create_engine(DATABASE_URL)
# async_engine = create_async_engine(DATABASE_URL_ASYNC, echo=False)
#
# # session_sync = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# session_async = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
# Base = declarative_base()
#
# async def get_db():
#     db = session_async()
#     try:
#         yield db
#     finally:
#         await db.close()
#
#
# # async def get_db_async():
# #     async with session_async() as session:
# #         query = select(Book).filter(**kwargs)
# #         await session.execute(query)

DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



