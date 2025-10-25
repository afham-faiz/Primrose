from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI app
app = FastAPI(title="Primrose API", version="1.0.0")

# Enable CORS so your frontend can talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, change this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic health check route
@app.get("/")
def root():
    return {"message": "Welcome to Primrose API"}

# Ping route to test if server is running
@app.get("/ping")
def ping():
    return {"message": "pong"}