from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'mssql+pyodbc://DESKTOP-O6MHKP8/proiect?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'

engine = create_engine(DATABASE_URL)

# Test connection
try:
    with engine.connect() as connection:
        print("Database connected successfully!")
except Exception as e:
    print(f"Error connecting to database: {e}")

