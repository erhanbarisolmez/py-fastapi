from pydantic import BaseModel, HttpUrl, Field, EmailStr
from enum import Enum

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"

class Image(BaseModel):
  url:HttpUrl
  name: str
  

class Car(BaseModel):
  name:str
  description: str | None = Field(default= None, examples=["A black  car"])
  price: float = Field(examples = [33.5])
  tax: float | None = Field(examples= [3.2])
  tags: set[str] = set()
  image: list[Image] |None = None
  

class Offer(BaseModel):
  name: str
  description: str | None = None
  price: float
  items: list[Car]
  
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float = 10.5
  tags: list[str] = [] 
  

class BaseProduct(BaseModel):
  username: str
  email: EmailStr
  full_name:str | None = None
   
  

class ProductIn(BaseProduct):
  password: str
  
class ProductInDB(BaseProduct):
  hashed_password:str
  


class CarBaseItem(BaseModel):
  description : str
  type: str
  
class CarItem(CarBaseItem):
  type: str= "car"
  
class PlaneItem(CarBaseItem):
  type: str = "plane"
  size: int
  
class lItem(BaseModel):
  name:str
  description: str
  