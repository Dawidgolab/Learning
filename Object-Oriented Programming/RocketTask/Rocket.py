# Rocket task
from random import randint
from math import sqrt

class Rocket:

# there are the static fields
    
    def __init__(self,speed=1,altitude = 0):
        self.altitude = altitude #start altitude
        self.speed = randint(0,4)
        self.x = 0
        # make patrol function
       
    def move_up(self):
        self.altitude += self.speed # move altitude

    def __str__(self): #function which visualize the object instead of ..at 0x... we can see the string
        return f"Rocket's current altitude: {self.altitude}"
    

class RocketBoard:
    def __init__(self,amountOfRockets=5):
        self.rockets = [Rocket(randint(1,6)) for _ in range(amountOfRockets)] # these are (from 0 to 4) objects 

        for _ in range(10):
            rocketIndexToMove = randint(0,len(self.rockets) - 1 ) #random rocket
            self.rockets[rocketIndexToMove].move_up() # random rocket move up

        for value ,rocket in enumerate(self.rockets):
            print(f"(Rocket index[{value}]) {rocket}")
        
        print("---------------------------------------------")

    def __getitem__(self,key): # we refer to the index 
        return self.rockets[key]
    
    def __setitem__(self,key,value): # we refer to the index but we also assign something to the value(e.g. from the index)
        self.rockets[key].altitude = value

    @staticmethod #static method without self
    def get_distance(rocket1,rocket2):
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.altitude - rocket2.x) ** 2
        return sqrt(ab + bc)