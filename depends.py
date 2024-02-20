from typing import Annotated
from fastapi import Depends, FastAPI, Cookie, HTTPException, Header

class CommonQueryParams:
  def __init__(self, q:str | None = None, skip: int=0, limit: int=100):
    self.q = q
    self.skip = skip
    self.limit = limit
    

async def verify_token(x_token: Annotated[str, Header()]):
  if x_token != "fake-super-secret-token":
    raise HTTPException(status_code=400, detail="X-Token header invalid")
  
async def verify_key(x_key: Annotated[str, Header()]):
  if x_key != "fake-super-secret-key":
    raise HTTPException(status_code=400, detail="X-Key header invalid")
  return x_key

app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
  response = {}
  if commons.q:
    response.update({"q": commons.q})
  items = fake_items_db[commons.skip : commons.skip + commons.limit]
  response.update({"items": items})
  return response

def query_extractor(q:str | None = None):
  return q

def query_or_cookie_extractor(
  q: Annotated[str, Depends(query_extractor)],
  last_query: Annotated[str | None, Cookie()] = None
):
  if  not q:
    return last_query
  return q

@app.get("/items/")
async def read_query(
  query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
):
  return {"q_or_cookie": query_or_default}


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
  return [{"item": "Foo"}, {"item": "Bar"}]

#app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
@app.get("/items2/")
async def read_items():
  return [{"item": "Foo"}, {"item": "Bar"}]

async def get_db():
  db= DBSession()
  try:
    yield db
  finally:
    db.close()
    
class MySuperContextManager:
    def __init__(self):
      self.db = DBSession()
      
    def __enter__(self):
      return self.db
    
    def __exit__(self, exc_type, exc_value, traceback):
      self.db.close()
      
async def get_db():
  with MySuperContextManager() as db:
    yield db


