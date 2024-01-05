"""
1. Make a menu where we ask if I want to display facts about dogs or cats
2. Display random 5 facts
"""

import requests
import json
from pprint import pprint

def param_cat():
    params = {
    "animal_type" : "cat",
    "amount" : 5
    }
    return params

def param_dog():
    params = {
        "animal_type" : "dog",
        "amount" : 5
    }
    return params

def url_json(param):
    r = requests.get('https://cat-fact.herokuapp.com/facts/random',param)
    try:
        facts = r.json()
    except json.decoder.JSONDecodeError:
        print("Invalid format!!!")
    else:
        for i, fact in enumerate(facts, start=1):
            print(f"{i}. {fact['text']}")




while True:
    choice = int(input("Select 5 fact about : 1 - dogs or 2 - cats: "))
#dogs
    if choice == 1:
        url_json(param_dog())
        break
#cats
    elif choice == 2:
        url_json(param_cat())
        break
#The next attempt
    else:
        print("Try again!!!")
        continue





