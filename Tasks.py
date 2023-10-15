#task 1
'''Write a function that will simulate how the lotto works
– you choose 6 unique numbers out of 49'''

'''import random

lottoList = []
def randomNumbers(number_list):
    while len(number_list) < 6:
        randNum = random.randint(0,49)
        if randNum not in lottoList:
            lottoList.append(randNum)
    return lottoList

print(randomNumbers(lottoList))'''

#task 2
'''1.Write a short game in which you have 5 moves one way through a chamber.
2.Each time you have a chance to encounter a chest or nothing in your path.
3. the chests have different colors
4. the color of a chest indicates its rarity:
- green - 75%
- Orange - 20%
- Purple - 4%
- Gold (legendary) - 1%

5. Set, 40% chance you won't meet anything. 60% chance that the chest will appear.
6. Set gold chest, what exactly can fall out of it
- green - 1000
- orange - 4000
- purple - 9000
- gold - 16000
'''

import random


Prize = ["You have draw a chest" ,"you have draw nothing"]
Chest = ['Green','Orange','Purple','Gold']

print("Welcome in my game called Chamber")
print("you have only 5 steps to make,"
      "see yourself how much gold you gonna acquire till the end !!!")

gamerChoice = 1

while gamerChoice <= 8:
    gamerChoice += 1
    step = input("Do you want to move forward (please select yes/no):  \n")
#Main option 'yes'
    if step == 'yes':
        print("Great , let's see what you got ...")
        stepYes = random.choice(Prize)
        print(stepYes)
        if stepYes == Prize[0]:
            importanceOfTheBox = random.choices(Chest,[75,20,4,1],k = 100)
            print("The chest color is :",random.choice(importanceOfTheBox))
#Finish the program
    elif step == 'no':
        break
        print("Good bye")
#What we use the other options
    else:
        print("You've chosen the wrong option, try again:\n")
        gamerChoice -= 1
        continue
