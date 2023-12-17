# database.py
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost/ahorros"

database = Database(DATABASE_URL)
metadata = declarative_base()

engine = create_engine(DATABASE_URL)
metadata.create_all(bind=engine)
