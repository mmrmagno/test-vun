from passlib.context import CryptContext
from app.models import users
from app.database import database

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify_password(plain_password, hashed_password)

async def authenticate_user(username: str, password: str):
    query = users.select().where(users.c.username == username)
    user = await database.fetch_one(query)
    if user and verify_password(password, user["password"]):
        return True
    return False