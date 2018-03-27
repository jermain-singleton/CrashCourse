class Users():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.login_attempts = 0

    def describe_user(self):
        fullname = self.first + " " + self.last
        print(fullname.title() + " is the user.")

    def greet_user(self):
        fullname = "Mr. " + self.first + " " + self.last
        print(fullname.title() + ", nice to see you come in.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(Users):
    """Represents a admin in the user class."""
    def __init__(self, first, last):
        self.privileges = []
        """Initialize attribute of parent class."""
        super().__init__(first, last)
        self.privileges = Privileges()

    

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in Call1.privileges:
            print(privilege)

Call1 = Admin("Germain", "Singleton")
Call1.privileges = ['can add', 'can query', 'can remove']
# Call1.greet_user()

# Call2 = Privileges()
# Call2.privileges = Call1.privileges
# Call2.show_privileges()
