class UserManager:
    def __init__(self):
        self.current_user = "student"

    def login(self):
        name = input("Enter username: ")
        if name:
            self.current_user = name
            print(f"Welcome {self.current_user}")
            return True
        return False