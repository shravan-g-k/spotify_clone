import uuid
import bcrypt
from fastapi import Depends, HTTPException
from models.user import User
from pydantic_schemas.user_create import UserCreate 
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session

from pydantic_schemas.user_login import UserLogin

router = APIRouter()
@router.post("/signup",status_code=201)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hased_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), name=user.name, email=user.email, password=hased_pw)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db


@router.post("/login")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    
    user_db = db.query(User).filter(User.email==user.email).first()

    if not user_db:
        raise HTTPException(400,"No user found")
    
    is_match = bcrypt.checkpw(user.password.encode(),user_db.password)

    if not is_match:
        raise HTTPException(400,"Incorrect password")
    
    return user_db

