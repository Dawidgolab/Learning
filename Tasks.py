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


myAccount = 0
Prize = ["Congratulations! You've found a chest!", "Unfortunately, you found nothing."]


Chest1 = {'Color':'Green', 'Points': 1000}
Chest2 = {'Color':'Orange', 'Points': 4000}
Chest3 = {'Color':'Purple' ,'Points': 9000}
Chest4 = {'Color':'Gold', 'Points': 16000}
Chests = [Chest1,Chest2,Chest3,Chest4]

print("Welcome in my game")
print("You have only 5 moves left. Let's see how much treasure you can uncover!")


gamerChoice = 1

while gamerChoice <= 5:
    print(f"Move {gamerChoice}:")
    step = input("Do you wish to move forward? (Type 'yes' or 'no'):  \n")
    gamerChoice += 1

#Main option 'yes'
    if step == 'yes':
        print("Alright, let's see what destiny has in store for you...")
        percentageStep = random.choices(Prize,[60,40],k = 100)
        stepYesOrNo = random.choice(percentageStep)
        print(stepYesOrNo)

        if stepYesOrNo == Prize[0]:
            percentageOfTheBox = random.choices(Chests,[75,20,4,1],k = 100 )
            kindOfTheBox = random.choice(percentageOfTheBox)
            print("You've discovered :", kindOfTheBox['Color'])
            myAccount += kindOfTheBox['Points']
            print("Added points to my account!!!")
            if gamerChoice > 5:
                print("My points scored:", myAccount)

#Finish the program
    elif step == 'no':
        print("Goodbye! Thanks for playing.")
        break

#What if we use the other options
    else:
        print("Sorry, you've selected an invalid option. Please try again:\n")
        gamerChoice -= 1
        continue
