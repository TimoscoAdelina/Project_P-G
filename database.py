# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = 'mssql+pyodbc://DESKTOP-O6MHKP8/proiect?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'

# engine = create_engine(DATABASE_URL)
# Base = declarative_base()
# # Test connection
# try:
#     with engine.connect() as connection:
#         print("Database connected successfully!")
# except Exception as e:
#     print(f"Error connecting to database: {e}")


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL conexiune SQL Server
DATABASE_URL = "mssql+pyodbc://DESKTOP-SC82VPV/proiect?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

# Creează engine-ul (conexiunea)
engine = create_engine(DATABASE_URL)

# Test conexiune
try:
    with engine.connect() as connection:
        print("✅ Database connected successfully!")
except Exception as e:
    print(f"Error connecting to database: {e}")

# Creează sesiuni pentru query-uri
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baza pentru toate modelele (ORM)
Base = declarative_base()

# Dependency pentru FastAPI (gestionare sesiuni)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()









