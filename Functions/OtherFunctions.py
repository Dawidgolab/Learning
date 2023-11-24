# split - we can separate two words
full_name = "Marek Kowalski"
print(full_name .split()[0],"\n")

#collections with Counter - count the elements and create dictionary
from collections import Counter

list = [1,2,3,4,5,6,7,8,9,10]

def evenNumbers(list):
    return [number for number in list if number % 2 == 0]

print(Counter(evenNumbers(list)))

#Approximate funtion

import random
def findApproximate(value,percentRange):
    lowestValue = value - (value * percentRange )/100
    higherValue = value + (value * percentRange) / 100
    return random.randint(lowestValue,higherValue)

print(findApproximate(1000,10))
