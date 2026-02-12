from datetime import datetime, timedelta
from database.connection import SessionLocal
from database.models import User


@app.post("/create-user/")
def create_user(telegram_id: int):
    db = SessionLocal()
    expiry = datetime.utcnow() + timedelta(days=30)

    user = User(
        telegram_id=telegram_id,
        subscription_expiry=expiry
    )

    db.add(user)
    db.commit()
    db.close()

    return {"status": "User Created", "expires": expiry}
