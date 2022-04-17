from fastapi import APIRouter, Depends, HTTPException, status
from core.security import verify_password
from models.login import Login
from repositories.users import UserRepository
from routes.depends import get_user_repository

router = APIRouter()

@router.post("/")
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.Password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect Email or Password")
    return {"Email": user.Email, "Message": "Login Successful"}