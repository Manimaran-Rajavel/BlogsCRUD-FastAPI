from fastapi import FastAPI
import models as md
from database import engine
from routers import blogs
from routers import user



app = FastAPI()

md.Base.metadata.create_all(engine)

app.include_router(blogs.router)

app.include_router(user.router)