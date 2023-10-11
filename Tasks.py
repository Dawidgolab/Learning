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
- green - 75
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