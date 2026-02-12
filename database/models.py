from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    subscription_expiry = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
