from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import(
  OAuth2PasswordBearer,
  OAuth2PasswordRequestForm,
  SecurityScopes
)

from jose import JWTError, jwt
from passlib.context import CryptContext

from models import tokenModel, usersModel
from schemas import usersSchema,tokenSchema
from database.db import Base

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(
   tokenUrl="token",
    scopes={"me": "Read information about the current user.", "items": "Read items."},

)

app = FastAPI()