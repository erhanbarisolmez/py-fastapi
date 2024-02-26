from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from  database.db import Base
from models.tokenModel import Token

class User(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  username = Column(String)
  email = Column(String, unique=True, index=True)
  full_name = Column(String, index=True)
  disabled = Column(Boolean, index=True)
  
  userInDB = relationship("UserInDB", back_populates="userID")
  
  tokens = relationship(Token, back_populates="user")
  
class UserInDB(User):
  __tablename__ = "users_in_db"
  
  hashed_password= Column(String, index=True)
  
  userID = relationship("User", back_populates="userInDB")
  
  
