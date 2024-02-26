from fastapi import Depends, FastAPI,status

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

from .tags_metadata import tags_metadata


app = FastAPI(
  dependencies=[Depends(get_query_token)],
  openapi_tags= tags_metadata
  )



app.include_router(users.router)
app.include_router(items.router)
app.include_router(
  admin.router,
  prefix="/admin",
  tags=["admin"],
  dependencies=[Depends(get_token_header)],
  responses={status.HTTP_418_IM_A_TEAPOT: {"description": "I'm a teapot"}}
),


@app.get("/", tags=["admin"])
async def root():
  return {"message": "Hello Bigger Applications!"}

@app.get("/", tags=["users"])
async def asd():
  return {"message": "Hello Bigger Applications!"}




