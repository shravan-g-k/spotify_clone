
from fastapi import FastAPI
from server.database import engine
from routes import auth
from server.models.base import Base 


app = FastAPI()

app.include_router(auth.router, prefix="/auth")

Base.metadata.create_all(engine)