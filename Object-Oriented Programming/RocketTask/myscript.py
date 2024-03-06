from random import randint
from Rocket import Rocket,RocketBoard

rockets = [Rocket(randint(1,6)) for _ in range(5)] # these are (from 0 to 4) objects 

for _ in range(10):
    rocketIndexToMove = randint(0,4) #random rocket
    rockets[rocketIndexToMove].move_up() # random rocket move up

print("Our 5 rockets after random(0,4) moves:")
for value ,rocket in enumerate(rockets,start=1):
    print(value,rocket)
