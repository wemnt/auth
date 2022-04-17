from typing import List, Optional
from core.security import hash_password
from .base import  BaseRepository
from datetime import datetime
from models.users import Users, UsersCreate, UserUpdate
from database.user import users


class UserRepository(BaseRepository):
    async def get_all(self, limit: int=100, skip: int=0) -> List[Users]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def get_by_id(self, id: int) -> Optional[Users]:
        query = users.select().where(users.c.ID == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return Users.parse_obj(user)

    async def get_by_email(self, email: str) -> Optional[Users]:
        query = users.select().where(users.c.Email == email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return Users.parse_obj(user)

    async def create(self, user: UsersCreate) -> Users:
        user = Users(
            Username=user.Username,
            Email=user.Email,
            Password=hash_password(user.Password),
            Created_at=datetime.utcnow(),
            Updated_at=datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("ID", None)
        query = users.insert().values(**values)
        user.ID = await self.database.execute(query)
        return user

    async def update(self, id: int, user: UserUpdate) -> Users:
        user = Users(
            ID=id,
            Username=user.Username,
            Email=user.Email,
            Password=user.Password,
            Created_at=datetime.utcnow(),
            Updated_at=datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("ID", None)
        values.pop("Created_at", None)
        if user.Password is None:
            values.pop("Password")
        query = users.update().where(users.c.ID==id).values(**values)
        await self.database.execute(query)
        return user