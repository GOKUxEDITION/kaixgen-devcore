class AccessControl:
    def __init__(self):
        self.allowed_users = []

    def validate_user(self, user_id: int) -> bool:
        return user_id in self.allowed_users
