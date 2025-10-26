from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

# User Model
class User(SQLModel, table=True):
    """A user who creates and studies flashcard decks"""
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True)
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Relationship: A user can have many decks
    decks: List["Deck"] = Relationship(back_populates="owner")

# Deck Model
class Deck(SQLModel, table=True):
    """A collection of flashcards on a specific topic"""
    __tablename__ = "decks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    last_studied: Optional[datetime] = None
    
    # Foreign key: Links deck to a user
    user_id: int = Field(foreign_key="users.id")
    
    # Relationships
    owner: Optional[User] = Relationship(back_populates="decks")
    cards: List["Card"] = Relationship(back_populates="deck")

# Card Model
class Card(SQLModel, table=True):
    """Individual flashcard with front and back content"""
    __tablename__ = "cards"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    front: str  # Question or prompt
    back: str   # Answer
    
    # Spaced repetition fields
    ease_factor: float = Field(default=2.5)  # How easy the card is (used in algorithm)
    interval_days: int = Field(default=0)    # Days until next review
    repetitions: int = Field(default=0)      # Number of times reviewed
    last_reviewed: Optional[datetime] = None
    next_review: Optional[datetime] = None
    
    # Foreign key: Links card to a deck
    deck_id: int = Field(foreign_key="decks.id")
    
    # Relationship
    deck: Optional[Deck] = Relationship(back_populates="cards")