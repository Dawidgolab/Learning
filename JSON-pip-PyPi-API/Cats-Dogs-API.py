"""
Task 1
1. Make a menu where we ask if I want to display facts about dogs or cats
2. Display random 5 facts

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
"""

"""
Task 2 
1. Make a program which download 3 records about the cats
2. After program start , display the url on the webside
"""



import requests
import webbrowser
import json
import pprint

catsLimit = int(input("Input the cats limit: "))

params = {
    "limit" : catsLimit
}

link = requests.get("https://api.thecatapi.com/v1/images/search", params)

try:
    respond = link.json()
except requests.RequestException as e:
    print(f"Request failed: {e}")
except json.JSONDecodeError as e:
    print(f"JSON decoding failed: {e}")
else:
    for i,picture in enumerate(respond):
        if i < catsLimit:
            webbrowser.open_new_tab(picture["url"])