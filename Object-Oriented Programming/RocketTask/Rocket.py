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
    pass




