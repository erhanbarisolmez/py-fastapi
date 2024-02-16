from typing import Dict, Optional, List, Union
from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
  id:int
  name:str = "Erhan Barış"
  signup_ts: Union[datetime, None] = None
  friends: List[int] = []

external_data = {
  "id": "123",
  "signup_ts": "2021-08-15T17:49:06",
  "friends":  [1, "2", b"3"]
}

user = User(**external_data)
print(user)

def process_item(prices: Dict[str, float]):
  for item_name, item_price in prices.items():
    print(item_name)
    print(item_price)

def say_hi(name: Optional[str] = None):
  if name is not None:
    print(f"Hey {name}")
  else:
    print("Hello World")


class Person:
  def __init__(self, name:str):
    self.name = name

def get_person_name(one_person: Person):
  return one_person.name


