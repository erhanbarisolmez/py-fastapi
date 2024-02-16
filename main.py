from typing  import Union
from fastapi import FastAPI
from pydantic import BaseModel
from model.item import Item # örn from app.api.api_v1.endpoints import items, login, users, utils


app = FastAPI()


class Users(BaseModel):
  user_id: int
  name: str
  age: int

db = []
@app.get("/")
async def read_root():
  return {"hello" : "world"}

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, q:Union[str, None] = None):
  return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}", response_model=Item)
def update(item_id: int, item:Item):
  return{"item_name": item.pr, "item_id": item_id}

@app.get("/full_name")
def get_full_name(first_name, last_name):
  full_name = first_name.title() + " " + last_name.title()
  return {full_name}
print(get_full_name("John", "Doe"))

@app.put("/full_name", response_model=Item)
def get_full_name(first_name:str, last_name:str):
  db.append({"first_name": first_name, "last_name": last_name})
  full_name = first_name.title() + " " + last_name.title()
  return {full_name}


