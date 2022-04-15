from .connect import metadata, engine
from .user import users


metadata.create_all(bind=engine)
