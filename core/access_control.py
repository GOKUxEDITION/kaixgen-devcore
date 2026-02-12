from datetime import datetime
from database.connection import SessionLocal
from database.models import User


class AccessControl:

    def validate_user(self, user_id: int) -> bool:
        db = SessionLocal()
        user = db.query(User).filter(User.telegram_id == user_id).first()
        db.close()

        if not user:
            return False

        if not user.subscription_expiry:
            return False

        return user.subscription_expiry > datetime.utcnow()
