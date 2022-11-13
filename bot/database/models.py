from sqlalchemy import TIMESTAMP, VARCHAR, Column, ForeignKey, Integer, Boolean

from database.database import Base


class IdMixin(object):
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(Base):
    __tablename__ = "users"

    telegram_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)

