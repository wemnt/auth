import sqlalchemy
from .connect import metadata
import datetime

users = sqlalchemy.Table(
    "Users",
    metadata,
    sqlalchemy.Column('ID', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('Email', sqlalchemy.String, unique=True),
    sqlalchemy.Column('Username', sqlalchemy.String, unique=True),
    sqlalchemy.Column('Password', sqlalchemy.String),
    sqlalchemy.Column('Created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
    sqlalchemy.Column('Updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
)
