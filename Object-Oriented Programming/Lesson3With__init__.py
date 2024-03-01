'''
__init__ -> initialization , it means that we set the start's value for attribute
 - __init__ is where you specify what information you need to create a new thing (such as type and color) and what to do with it.

 *In the other languages the init == constructor 
'''

class User:
    name = ""
    age = 0
################## Initializator/ contructor ##################
    def __init__(self,name,age):
        print("Initializator!!!")

        self.name = name
        self.age = age
        self.ageInFuture = age + 1
#############################################################     

    def print_age(self):
        print(f"Name: {self.name}, Age: {self.age}, Your age after 1 year: {self.ageInFuture}")


user1 = User("Marek",24)
user2 = User("Darek", 20)

#user1.name = "Marek"
#user1.age = 25
user1.print_age()

#user2.name = "Darek"
#user2.age = 20
user2.print_age()
