import uuid
import bcrypt
from fastapi import HTTPException
from server.models.user import User
from server.pydantic_schemas.user_create import UserCreate 
from fastapi import APIRouter

router = APIRouter()
@router.post("/signup")
async def root(user: UserCreate):
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hased_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), name=user.name, email=user.email, password=hased_pw)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db
