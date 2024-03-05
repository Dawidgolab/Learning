# Rocket task
from random import randint

class Rocket:

    def __init__(self,speed=1):
        self.altitude = 0 #start altitude
        self.speed = randint(0,4)
       
        
    def move_up(self):
        self.altitude += self.speed # move altitude
    

    def __str__(self): #function which visualize the object instead of ..at 0x... we can see the string
        return f"Current altitude of rocket: {self.altitude}"


rockets = [Rocket(randint(1,6)) for _ in range(5)] # these are (from 0 to 4) objects 

for _ in range(10):
    rocketIndexToMove = randint(0,4) #random rocket
    rockets[rocketIndexToMove].move_up() # random rocket move up

print("Our 5 rockets after random(0,4) moves:")
for value ,rocket in enumerate(rockets,start=1):
    print(value,rocket)



