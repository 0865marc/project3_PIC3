from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/")
async def update_item(item: Item):
    return item

@app.delete("/item/{item_id}")
async def deletem_item(item_id: int):
    return {'item_id': item_id}