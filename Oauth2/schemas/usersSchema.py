from pydantic import BaseModel
from schemas.tokenSchema import Token

class UserBase(BaseModel):
  username: str
  email: str
  full_name: str
  disabled: bool
  
class UserCreate(UserBase):
  password: str
  
class User(UserBase):
  id: int
  tokens: list[Token] = []
  
  class Config: 
    from_attributes = True
    
class UserInDB(UserBase):
  hashed_password: str