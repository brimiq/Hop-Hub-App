from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection URL (SQLite for MVP)
DATABASE_URL = "sqlite:///taxi.db"

# Create engine to connect Python ↔ database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory: generates new database sessions
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models (tables)
Base = declarative_base()

# Dependency function for FastAPI endpoints
def get_db():
    db = session_local()  # open session
    try:
        yield db           # provide session to route
    finally:
        db.close()         # ensure session is closed
