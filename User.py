class User:
    """A simple attempt to simulate a user"""
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def describe_user(self):
        """An attempt to describe the user"""
        print(f"User information: {self.first_name} {self.last_name}, a {self.gender}")

    def greet_user(self):
        """An attempt to greet the user"""
        print(f"Good day {self.first_name}!! Have a great day!")

first_user = User("Jennylyn", "Mercado", "Female")
second_user = User("Dennis", "Trillo", "Male")

first_user.describe_user()
second_user.describe_user()

first_user.greet_user()
second_user.greet_user()

class Admin(User):
    """A simple attempt to simulate an admin of a software"""
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.priveleges = {
            'admin' : ["Can add post", "Can delete post", "Can ban user"],
        }

    def user_auth(self):
        """An attempt to display authority of users"""
        print(f"{self.first_name} {self.last_name} has the auth of an admin and can do the ff:")
        for auth in self.priveleges['admin']:
            print(f"\nAdmin:" + auth)

third_user = Admin("Melissa", "Benioif", "Female")
third_user.greet_user()
third_user.user_auth()