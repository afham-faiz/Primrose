from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from typing import List

# Import your models and database
from backend.database import init_db, get_session
from backend.models.models import User, Deck, Card

# Create the FastAPI app
app = FastAPI(title="Primrose API", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database when app starts
@app.on_event("startup")
def on_startup():
    init_db()
    print("Database initialized!")

# Basic routes
@app.get("/")
def root():
    return {"message": "Welcome to Primrose API"}

# Ping route to test if server is running
@app.get("/ping")
def ping():
    return {"message": "pong"}

# ============== USER ROUTES ==============

@app.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    """Create a new user"""
    session.add(user)
    session.commit()
    session.refresh(user)  # Get the ID that was auto-generated
    return user

@app.get("/users/", response_model=List[User])
def get_users(session: Session = Depends(get_session)):
    """Get all users"""
    users = session.exec(select(User)).all()
    return users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    """Get a specific user by ID"""
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    """Delete a user"""
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User deleted"}

# ============== DECK ROUTES ==============

@app.post("/decks/", response_model=Deck)
def create_deck(deck: Deck, session: Session = Depends(get_session)):
    """Create a new deck"""
    session.add(deck)
    session.commit()
    session.refresh(deck)
    return deck

@app.get("/users/{user_id}/decks", response_model=List[Deck])
def get_user_decks(user_id: int, session: Session = Depends(get_session)):
    """Get all decks for a specific user"""
    decks = session.exec(select(Deck).where(Deck.user_id == user_id)).all()
    return decks

@app.get("/decks/{deck_id}", response_model=Deck)
def get_deck(deck_id: int, session: Session = Depends(get_session)):
    """Get a specific deck"""
    deck = session.get(Deck, deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    return deck

@app.put("/decks/{deck_id}", response_model=Deck)
def update_deck(deck_id: int, deck_update: Deck, session: Session = Depends(get_session)):
    """Update a deck"""
    deck = session.get(Deck, deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    
    # Update fields
    deck.title = deck_update.title
    deck.description = deck_update.description
    
    session.add(deck)
    session.commit()
    session.refresh(deck)
    return deck

@app.delete("/decks/{deck_id}")
def delete_deck(deck_id: int, session: Session = Depends(get_session)):
    """Delete a deck and all its cards"""
    deck = session.get(Deck, deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    session.delete(deck)
    session.commit()
    return {"message": "Deck deleted"}

# ============== CARD ROUTES ==============

@app.post("/decks/{deck_id}/cards", response_model=Card)
def create_card(deck_id: int, card: Card, session: Session = Depends(get_session)):
    """Add a card to a deck"""
    card.deck_id = deck_id
    session.add(card)
    session.commit()
    session.refresh(card)
    return card

@app.get("/decks/{deck_id}/cards", response_model=List[Card])
def get_deck_cards(deck_id: int, session: Session = Depends(get_session)):
    """Get all cards in a deck"""
    cards = session.exec(select(Card).where(Card.deck_id == deck_id)).all()
    return cards

@app.put("/cards/{card_id}", response_model=Card)
def update_card(card_id: int, card_update: Card, session: Session = Depends(get_session)):
    """Update a card"""
    card = session.get(Card, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    card.front = card_update.front
    card.back = card_update.back
    
    session.add(card)
    session.commit()
    session.refresh(card)
    return card

@app.delete("/cards/{card_id}")
def delete_card(card_id: int, session: Session = Depends(get_session)):
    """Delete a card"""
    card = session.get(Card, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    session.delete(card)
    session.commit()
    return {"message": "Card deleted"}