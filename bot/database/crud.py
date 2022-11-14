from datetime import datetime
from typing import Optional

from database.database import SessionLocal
from database.models import User


def create_user(telegram_id: int, username: Optional[str], referer: Optional[int]) -> User:
    with SessionLocal() as session:
        db_user = User(
            telegram_id=telegram_id, name=username,referer=referer
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


def get_user(user_id: int):
    with SessionLocal() as session:
        session.query(User).filter(User.telegram_id == user_id).first()
        session.commit()
