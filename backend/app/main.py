# backend/app/main.py
from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI(title="Kenya Taxi Comparison App")

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Backend is working!"}
