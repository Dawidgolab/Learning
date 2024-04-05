'''
class parent - class child

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says something.")

class Dog(Animal):
    def wag_tail(self):
        print(f"{self.name} wags its tail.")

class Cat(Animal):
    def purr(self):
        print(f"{self.name} purrs softly.")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Output: Buddy says something.
cat.speak()  # Output: Whiskers says something.

dog.wag_tail()  # Output: Buddy wags its tail.
cat.purr()      # Output: Whiskers purrs softly.
'''