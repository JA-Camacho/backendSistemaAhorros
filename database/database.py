from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost/ahorros"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

clientes = Table(
    "clientes",
    metadata,
    Column("id_cliente", Integer, primary_key=True, index=True),
    Column("nombre", String, index=True),
    Column("correo_electronico", String, index=True),
    Column("password", String, index=True)
)

@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

async def execute(query, values=None):
    async with database.transaction():
        return await database.execute(query, values=values)

async def fetch_one(query, values=None):
    async with database.transaction():
        return await database.fetch_one(query, values=values)

async def fetch_all(query, values=None):
    async with database.transaction():
        return await database.fetch_all(query, values=values)
