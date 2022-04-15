from typing import Optional
from pydantic import BaseModel, EmailStr, constr, validator
from datetime import datetime

class Users(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    username: constr(min_length=4)
    password: Optional[str]
    created_at: datetime
    updated_at: datetime


class UsersCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=4)
    password: constr(min_length=6)
    password2: constr(min_length=6)

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("Password don`t match")
        return v


class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    password: Optional[constr(min_length=8)] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime