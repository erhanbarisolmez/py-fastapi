from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.db import Base
from models.usersModel import User

class Token(Base):
  __tablename__ = "tokens"
  
  access_token = Column(String, primary_key=True)
  token_type = Column(String, index=True)
  token_id = Column(Integer, ForeignKey(User.id))
 
token_data = relationship("TokenData", back_populates="token_id")

user = relationship(User, back_populates="tokens")
  
class TokenData(Base):
  __tablename__ = "token_data"
  
  username = Column(String, primary_key=True)
  scopes = Column(String, index=True)
  token_id = relationship("Token", back_populates="token_data")