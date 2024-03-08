# Rocket task
from random import randint

class Rocket:

    def __init__(self,speed=1):
        self.altitude = 0 #start altitude
        self.speed = randint(0,4)
       
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

    def __getitem__(self,key):
        return self.rockets[key]