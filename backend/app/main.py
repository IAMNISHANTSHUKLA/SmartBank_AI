from fastapi import FastAPI
from app.routers import auth, transactions, suggestions
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(transactions.router)
app.include_router(suggestions.router)

@app.get("/")
async def root():
    return {"message": "Welcome to SmartBankAI!"}
