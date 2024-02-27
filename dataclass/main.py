from dataclasses import  field
from typing import Union, List

from fastapi import FastAPI
from pydantic.dataclasses import dataclass

@dataclass
class Item:
  name: str
  price:float
  tags: List[str] = field(default_factory= list)
  description: Union[str, None] = None
  tax : Union[float, None] = None
  
  
app = FastAPI()


@app.post("/items/next", response_model=Item)
async def read_next_item():
  return {
    "name": "Island In The Moon",
    "price": 12.99,
    "description": "A place to be be  playin' and havin' fun",
    "tags": ["breater"],
  }