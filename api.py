from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Initialize FastAPI app
app = FastAPI()

# Define a data model using Pydantic
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    on_offer: bool

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app deployed on Vercel!"}

# Get item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

# Create a new item
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}

# Vercel requires a specific entry point file
# Rename this file to 'api.py' before deploying to Vercel
