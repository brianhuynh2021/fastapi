from os import access
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass

class Post(PostCreate):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True
        
class User(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True
        
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None