from sqlalchemy import TIMESTAMP, VARCHAR, Column, ForeignKey, Integer, Boolean

from database.database import Base


class IdMixin(object):
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(Base):
    __tablename__ = "users"

    telegram_id = Column(VARCHAR, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    first_buy = Column(Boolean, default=False, nullable=False)
    referer = Column(VARCHAR, nullable=True)
    discount_bonuses = Column(Integer, default=0)
