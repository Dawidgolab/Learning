# Rocket task
from random import randint

class Rocket:
    def __init__(self):
        self.altitude = 0 #start altitude
    
    def move_up(self):
        self.altitude += 1 # move altitude



rockets = [Rocket() for _ in range(5)] # these are (from 0 to 4) objects 

for _ in range(10):
    rocketIndexToMove = randint(0,4) #random rocket
    rockets[rocketIndexToMove].move_up() # random rocket move up

for rocket in rockets:
    print(rocket.altitude)

