"""
1. Make a menu where we ask if I want to display facts about dogs or cats
2. Display random 5 facts
"""

import requests
import json
from pprint import pprint


def cat_dog(animal):
    params = {
        "animal_type" : animal,
        "amount" : 5
    }
    return params


def url_json(params):
    r = requests.get('https://cat-fact.herokuapp.com/facts/random',params)
    try:
        facts = r.json()
    except json.decoder.JSONDecodeError:
        print("Invalid format!!!")
    else:
        for i, fact in enumerate(facts, start=1):
            print(f"{i}. {fact['text']}")



while True:
    choice = int(input("Select 5 fact about : 1 - cats or 2 - dogs: "))
#cats
    if choice == 1:
        animal = "cat"
        url_json(cat_dog(animal))
        break
#dogs
    elif choice == 2:
        animal = "dog"
        url_json(cat_dog(animal))
        break
#The next attempt
    else:
        print("Try again!!!")
        continue





