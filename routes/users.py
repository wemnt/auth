from typing import List
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from models.users import UserResponse, UsersCreate
from .depends import get_user_repository
from repositories.users import UserRepository

router = APIRouter()


@router.get("/", response_model=List[UserResponse])
async def get_all_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0):
    return await users.get_all(limit, skip)


@router.post("/", response_model=UserResponse)
async def create(
        user: UsersCreate,
        users: UserRepository = Depends(get_user_repository)):
    if users.get_by_email(user.Email) is not None:
        new_user = await users.create(user)
    else:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                             detail="User with this Email already exist")
    return new_user
