from datetime import datetime, timedelta
from jose import jwt
from backend.config import settings
def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(hours=24)})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm="HS256")

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
