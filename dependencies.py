from fastapi import Security, HTTPException

from database import SessionLocal
from fastapi.security import APIKeyHeader

from config import settings


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_token(token: str = Security(APIKeyHeader(name="authorization"))):
    if settings.TOKEN != token:
        raise HTTPException(status_code=403, detail='invalid token')
