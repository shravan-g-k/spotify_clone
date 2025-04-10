from fastapi import FastAPI
from database import engine
from routes import auth
from models.base import Base 


app = FastAPI()

app.include_router(auth.router, prefix="/auth")

Base.metadata.create_all(engine)