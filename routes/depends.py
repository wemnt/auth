from fastapi import Depends, HTTPException
from repositories.users import UserRepository
from database.connect import database

def get_user_repository() -> UserRepository:
    return UserRepository(database)
