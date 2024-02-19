from typing import Annotated, List, Union, Any
from fastapi import FastAPI, Query, Path, Body, Header, Response, status, Form, File, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse
from model.ModelName import *
from pydantic import Field, BaseModel

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
  
  

@app.put("/put/{item_id}")
async def update_item(item_id: int, item: Annotated[Car, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
  
class Item(BaseModel):
  name: str
  description: str | None = Field(
    default=None, title="The description of the item", max_length=300
  )
  price: float = Field(gt=0, description="a")
  tax: float | None = None
  
@app.put("/asd/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
  results = {"item_id": item_id, "item": item}
  return results

@app.put("/cars/{car_id}")
async def update_car(car_id: int, item: Car):
  results = {"car_id": car_id, "Car": item}
  return results

@app.put("/l/{item_id}")
async def update_l(item_id: int, item: Car):
  results = {"item_id": item_id, "item": item}
  return results

@app.post("/offers/")
async def create_offer(offer: Offer):
  return offer

@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
  for image in images:
    image.name
  return images


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
  return weights

@app.get("/header/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
  return {"User-Agent" : user_agent}

@app.get("/xtoken/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
  return {"X-Token values" : x_token}

@app.post("/formdata/", response_model=Car)
async def create_item(item: Car) -> Any:
  return item

@app.get("/formdata/", response_model=list[Car])
async def read_items() -> Any:
  return [
    Car(name="BMW", price=52.9),
    Car(name="Mercedes", price=47.13)
  ]
  
@app.post("/Iuser")
async def create_user(user:UserIn) -> BaseUser:
  return user

@app.get("/portal")
async def get_portal(teleport:bool = False) -> Response:
  if teleport:
    return RedirectResponse(url="http://www.youtube.com")
  return JSONResponse(content={"message": "Here's your interdimensional portal."})

@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
  return RedirectResponse(url="https://youtube.com")


items = {
  "foo": {"name": "Foo", "price": 50.2},
  "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
  "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/ttt/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
  return items[item_id]

item = {
  "foo": {"name": "Foo", "price": 50.2},
  "bar": {"name": "Bar", "description": "The Bar Fighters", "price":55, "tax": 20.3},
  "baz": {
    "name": "Baz",
    "description": "There goes my baz",
    "price": 50.2,
    "tax": 10.4,
  }
}

@app.get(
  "/items/{item_id}/name",
  response_model=Item,
  response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
  return item[item_id]

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
  return item[item_id]


def fake_password_hasher(raw_password: str):
  return "supersecret" + raw_password

def fake_save_product(product_in: ProductIn):
  hashed_password = fake_password_hasher(product_in.password)
  product_in_db = ProductInDB(**product_in.model_dump(), hashed_password=hashed_password)
  print("Product saved! ..not really")
  return product_in_db

@app.get("/product2/", response_model=BaseProduct)
async def create_product(product_in: ProductIn) ->  ProductIn:
  product_saved = fake_save_product(product_in)
  return product_saved


itemCar = {
  "item1": {"description": "All my friends drive a low rider", "type": "car"},
  "item2": {
    "description": "Music is my aeroplane, it's my aeroplane",
    "type": "plane",
    "size": 5
  }
}

@app.get("/pp/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
  return itemCar[item_id]

iteml = [
  {"name" : "Foo", "description": "There comes my hero"},
  {"name" : "Red", "description": "There comes my red"}
]

@app.get("/ll/", response_model=list[lItem])
async def read_items():
  return iteml

@app.get("/keyword-weights/", response_model=dict[str, float])
async def keyword_weight(text: str):
  words = text.split()
  return words

@app.post("/itemsStatus/", status_code=status.HTTP_201_CREATED)
async def create_item(name:str):
  return {"name": name}


@app.post("/login/")
async def login(username: Annotated[str, Form()], password:Annotated[str, Form()]):
  return {"username": username, "password": password}

@app.post("/files/")
async def create_file(files: Annotated[list[bytes], File(description="Multiple files as bytes")]):
  return {"file_size": [len(file) for file in files]}

@app.post("/uploadfiles/")
async def create_upload_file(files: Annotated[ list[UploadFile], File(description="Multiple files as UploadFile")]):
  return {"filename": [file.filename for file in files]}


@app.post("/files2")
async def create_file(
  file: Annotated[bytes, File()],
  fileb: Annotated[UploadFile, File()],
  token: Annotated[str, Form()],
):
  return {
    "file_size": len(file),
    "token": token,
    "fileb_content_type": fileb.content_type
  }

