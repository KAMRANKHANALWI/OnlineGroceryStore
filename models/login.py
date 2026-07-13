class Login:

    def __init__(self, email, password, user_type, status, login_id=None):
        self.login_id = login_id
        self.email = email
        self.password = password
        self.user_type = user_type
        self.status = status

    def __str__(self):
        return (
            f"Login("
            f"login_id={self.login_id}, "
            f"email='{self.email}', "
            f"user_type='{self.user_type}', "
            f"status='{self.status}')"
        )
