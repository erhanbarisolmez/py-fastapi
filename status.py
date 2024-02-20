from fastapi import FastAPI, status, Depends
from pydantic import BaseModel
from enum import Enum
from fastapi.encoders import jsonable_encoder
from typing import Annotated

fake_db = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

app = FastAPI()
# ENUM
class Tags(Enum):
  items = "items"
  users = "users"
# MODEL
class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []

  
@app.post("/items/", 
  response_model=Item,
  status_code=status.HTTP_201_CREATED,
  summary="Create an Item",
  description="Create an item with all the information, name, description, price..."
  )
async def create_item(item: Item):
  return item

@app.post("/items_tags/", response_model=Item, tags=[Tags.items])
async def create_item(item: Item):
  """
      Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
  """
  return item

@app.get("/items_tags", tags=[Tags.items])
async def read_items():
  return [{"name": "Foo", "price": 42}]

@app.get("/users/", tags=[Tags.users], response_description="The created item")
async def read_users():
  return [{"username": "johndoe"}]

@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
  return [{"item_id": "Foo"}]

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
  
async def common_parameters(q:str | None = None, skip: int= 0, limit: int = 100):
  return {"q": q, "skip": skip, "limit": limit}

@app.get("/new_items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
  return commons

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
  return commons
