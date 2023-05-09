from typing import List, Optional
from pydantic import BaseModel

class Admin(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
        
class AdminCreate(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True

class Post(BaseModel):
    id: int
    title: str
    hashtags: str
    reading_time: str
    category: str
    description: str
    note: str
    code_space: str
    second_code_space: str
    is_active: bool
    created_at: str
    update_at: str

    class Config:
        orm_mode = True

class Snippet(BaseModel):
    id: int
    title: str
    image: str
    hashtags: str
    reading_time: str
    category: str
    description: str
    note: str
    code_space: str
    second_code_space: str
    is_active: bool
    created_at: str
    update_at: str

    class Config:
        orm_mode = True
        
class PostCreate(BaseModel):
    title: str
    hashtags: str
    reading_time: str
    category: str
    description: str
    note: str
    code_space: str
    second_code_space: str
    is_active: bool
    
    class Config:
        orm_mode = True
    
class SnippetCreate(BaseModel):
    title: str
    image: str
    hashtags: str
    reading_time: str
    category: str
    description: str
    note: str
    code_space: str
    second_code_space: str
    is_active: bool
    
    class Config:
        orm_mode = True
    
class PostUpdate(BaseModel):
    title: Optional[str] = None
    hashtags: Optional[str] = None
    reading_time: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    note: Optional[str] = None
    code_space: Optional[str] = None
    second_code_space: Optional[str] = None
    is_active: Optional[bool] = None
    
    class Config:
        orm_mode = True
    
class SnippetUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    hashtags: Optional[str] = None
    reading_time: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    note: Optional[str] = None
    code_space: Optional[str] = None
    second_code_space: Optional[str] = None
    is_active: Optional[bool] = None
    
    class Config:
        orm_mode = True
    
class PostDelete(BaseModel):
    id: int
    
    class Config:
        orm_mode = True
    
class SnippetDelete(BaseModel):
    id: int
    
    class Config:
        orm_mode = True

