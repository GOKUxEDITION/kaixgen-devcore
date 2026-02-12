class AccessControl:
    def __init__(self):
        # Example allowed users
        self.allowed_users = [123456]

    def validate_user(self, user_id: int) -> bool:
        return user_id in self.allowed_users
