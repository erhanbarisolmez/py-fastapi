from pydantic import BaseModel
from enum import Enum

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"


class Car(BaseModel):
  name:str
  description: str | None = None
  price: float
  tax: float | None = None

