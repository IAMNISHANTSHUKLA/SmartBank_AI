from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/add")
def add_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(database.SessionLocal)):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
