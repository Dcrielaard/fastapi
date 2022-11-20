import time
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"We except price >0, we received {value}")
        return value

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    """
    We accept a `user_id` here, and return a json-blob containing it.
    """
    return {"user_id": user_id}

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/sleep_slow")
def sleep_slow():
    r = time.sleep(1)
    return {"status": "done"}

@app.get("/sleep_fast")
async def sleep_fast():
    r = await asyncio.sleep(1)
    return {"status": "done"}

