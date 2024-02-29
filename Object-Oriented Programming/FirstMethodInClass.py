''' 'self' in python but 'this' in another languages '''


class User:
    name = ""
    age = 0

    def print_age(self):
        print(f"Name: {self.name}, Age: {self.age}")


user1 = User()
user2 = User()

user1.name = "Marek"
user1.age = 25
user1.print_age()

user2.name = "Darek"
user2.age = 20
user2.print_age()
