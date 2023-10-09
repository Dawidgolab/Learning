#task 1
'''Write a function that will simulate how the lotto works
– you choose 6 unique numbers out of 49'''

import random

lottoList = []
def randomNumbers(number_list):
    while len(number_list) < 6:
        randNum = random.randint(0,49)
        if randNum not in lottoList:
            lottoList.append(randNum)
    return lottoList

print(randomNumbers(lottoList))