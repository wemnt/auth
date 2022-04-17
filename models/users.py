from typing import Optional
from pydantic import BaseModel, EmailStr, constr, validator
from datetime import datetime

class Users(BaseModel):
    ID: Optional[int] = None
    Email: EmailStr
    Username: constr(min_length=4)
    Password: Optional[str]
    Created_at: datetime
    Updated_at: datetime


class UsersCreate(BaseModel):
    Email: EmailStr
    Username: constr(min_length=4)
    Password: constr(min_length=6)
    Password2: constr(min_length=6)

    @validator("Password2")
    def password_match(cls, v, values, **kwargs):
        if 'Password' in values and v != values["Password"]:
            raise ValueError("Password don`t match")
        return v


class UserUpdate(BaseModel):
    Username: str
    Email: EmailStr
    Password: Optional[constr(min_length=8)] = None


class UserResponse(BaseModel):
    ID: int
    Username: str
    Email: EmailStr
    Password: str
    Created_at: datetime
    Updated_at: datetime