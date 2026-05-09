from fastapi import FastAPI

app = FastAPI(title="Manufacturing Quality API")

@app.get("/")
def home():
    return {"message": "Manufacturing Quality API is running"}

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

app = FastAPI(title="Manufacturing Quality API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Manufacturing Quality API is running"}

@app.get("/identifiers", response_model=list[schemas.IdentifierResponse])
def read_identifiers(db: Session = Depends(get_db)):
    return crud.get_identifiers(db)

@app.get("/identifiers/{identifier_name}", response_model=schemas.IdentifierResponse)
def read_identifier(identifier_name: str, db: Session = Depends(get_db)):
    identifier = crud.get_identifier(db, identifier_name)

    if identifier is None:
        raise HTTPException(status_code=404, detail="Identifier not found")

    return identifier

@app.post("/identifiers", response_model=schemas.IdentifierResponse)
def create_identifier(
    identifier: schemas.IdentifierCreate,
    db: Session = Depends(get_db)
):
    return crud.create_identifier(db, identifier)

@app.delete("/identifiers/{identifier_name}")
def delete_identifier(identifier_name: str, db: Session = Depends(get_db)):
    deleted_identifier = crud.delete_identifier(db, identifier_name)

    if deleted_identifier is None:
        raise HTTPException(status_code=404, detail="Identifier not found")

    return {"message": "Identifier deleted successfully"}