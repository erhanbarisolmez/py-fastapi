from typing  import Union
from pydantic import BaseModel

class Item(BaseModel):
  name:str
  first_name:str
  last_name:str
  price:float
  is_offer: Union[bool, None] = None
  