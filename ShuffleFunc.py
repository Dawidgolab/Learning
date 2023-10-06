# shuffle - randomizes entire list( this works on the original list )

import random

cardList = ["9","9","9","9",
            "10","10","10","10",
            "Jack","Jack","Jack","Jack",
            "Queen","Queen","Queen","Queen",
            "King","King","King","King",
            "Ace", "Ace", "Ace", "Ace",
            "Jocker","Jocker"]

random.shuffle(cardList)
print(cardList)