from typing import Annotated
from fastapi import FastAPI, Query, Path
from model.ModelName import ModelName,Car



app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
  return {"message" : "..."}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {"item_id": item_id}

@app.get('/user/me')
async def read_user_me():
  return {'user_id': 'the current user'}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
  return {'user_id': user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
 
  if model_name is ModelName.alexnet:
    return {"model_name": model_name, "message" : "Deep Learning FTW"}
  
  if model_name.value == 'lenet':
    return {"model_name": model_name, "message": "LeCNN all the images"}
  
  return {" model_name" : model_name, "message": "Have some residuals"}

@app.get("/files/{files_path:path}")
async def read_file(file_path: str):
  return {"file_path": file_path}


@app.get("/product/")
async def read_item(skip: int = 0, limit: int = 10):
  return fake_items_db[skip: skip + limit]

@app.get("/product/{item_id}")
async def read_product(item_id:str, q:str | None = None, short: bool = False):
  item = {"item_id": item_id}
  if q:
    item.update({"q":q})
  if not short:
    item.update(
      {"description": "This is an amazing item that has a long desctription"}
    )
  return item

@app.get("/user/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q:str | None = None, short: bool = False
):
  item = {"item_id": item_id, "owner_id": user_id}
  if q:
    item.update({"q": q})
  if not short:
    item.update(
      {"desctription" : "Read _ user  _ item"}
    )
  if short:
    item.update(
      {"short":"Short var"}
    )
  return item


@app.get("/car/{car_id}")
async def read_car_item(car_id: str, needy: str, skip: int = 0, limit : int | None = None):
  item = {"car_id": car_id, "needy": needy, "skip": skip, "limit": limit}
  return item

@app.post("/car/add/")
async def create_item(item:Car):
  item_dict = item.model_dump()
  if item.tax:
    price_with_tax = item.price + item.tax
    item_dict.update({"price_with_tax": price_with_tax})
  return item_dict

@app.put("/car/{item_id}")
async def update_item(item_id:int, item: Car,q: str| None = None,):
  result = {"item_id": item_id, **item.dict()}
  if q:
    result.update({"q" : q})
  return result

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3,max_length=50)] = None):
  results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
  if q:
    results.update({"q":q})
  return results

@app.get("/asd/")
async def read_items(
  q:Annotated[
    str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
  ] = None,
):
  results = {"items" : [{"item_id": "Foo"}, {"item_id": "Bar"}]}
  if q:
    results.update({"q": q})
  return results


@app.get("/item2")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
  
  
@app.get("/r/{r_item}")
async def read_r(
    r_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
  ):
    results = {"r_item" : r_id}
    if q:
        results.update({"q": q})
    return results
  
