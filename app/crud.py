from sqlalchemy.orm import Session
from app import models, schemas

def get_identifiers(db: Session):
    return db.query(models.Identifier).all()

def get_identifier(db: Session, identifier_name: str):
    return db.query(models.Identifier).filter(
        models.Identifier.identifier_name == identifier_name
    ).first()

def create_identifier(db: Session, identifier: schemas.IdentifierCreate):
    db_identifier = models.Identifier(**identifier.model_dump())
    db.add(db_identifier)
    db.commit()
    db.refresh(db_identifier)
    return db_identifier

def delete_identifier(db: Session, identifier_name: str):
    db_identifier = get_identifier(db, identifier_name)

    if db_identifier:
        db.delete(db_identifier)
        db.commit()

    return db_identifier