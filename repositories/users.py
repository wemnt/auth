from typing import List, Optional
from .base import  BaseRepository
from datetime import datetime
from models.users import Users, UsersCreate, UserUpdate
from database.user import users

class UserRepository(BaseRepository):
    async def get_all(self, limit: int=100, skip: int=0) -> List[Users]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def get_by_id(self, id: int) -> Optional[Users]:
        pass

    async def get_by_email(self, email: str) -> Optional[Users]:
        pass

    async def create(self, user: UsersCreate) -> Users:
        user = Users(
            username=user.username,
            email=user.email,
            password=user.password,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, user: UserUpdate) -> Users:
        pass

