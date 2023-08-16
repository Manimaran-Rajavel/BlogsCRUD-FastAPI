from pydantic import BaseModel
from typing import List

class Blogs(BaseModel):
    title: str 
    body: str



class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blogs]

    class config():
        orm_mode = True

class ShowBlogs(BaseModel):
    title: str 
    body: str
    creater: ShowUser
    class config():
        orm_mode = True