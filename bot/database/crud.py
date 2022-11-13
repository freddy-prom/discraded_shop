from datetime import datetime
from typing import Optional

from database.database import SessionLocal
from database.models import User


def create_user(telegram_id: int, username: Optional[str]) -> User:
    with SessionLocal() as session:
        db_user = User(
            telegram_id=telegram_id, name=username,
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
