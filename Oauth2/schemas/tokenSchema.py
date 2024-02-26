from pydantic import BaseModel

class TokenBase(BaseModel):
  access_token: str
  token_type: str
  
class TokenCreate(TokenBase):
  pass

class Token(TokenBase):
  class Config: 
    from_attributes = True
    
class TokenData(BaseModel):
  username:str
  scopes: str
  

  
