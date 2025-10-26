from sqlmodel import SQLModel, Session, create_engine
import os

# SQLite database URL
# This creates a file called "primrose.db" in your backend folder
DATABASE_URL = "sqlite:///./primrose.db"

# Create the database engine
# connect_args={"check_same_thread": False} is needed for SQLite
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=True  # Set to True to see SQL queries in console (helpful for learning!)
)

def init_db():
    """Create all database tables"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Get a database session for each request"""
    with Session(engine) as session:
        yield session