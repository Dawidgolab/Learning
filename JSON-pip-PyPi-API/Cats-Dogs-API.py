"""
1. Make a menu where we ask if I want to display facts about dogs or cats
2. Display random 5 facts
"""

import requests
import webbrowser
import json
from pprint import pprint

params = {
    "animal_type" : "dog",
    "amount" : 3
}



r = requests.get('https://cat-fact.herokuapp.com/facts/random',params)

try:
    facts = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format!!!")
else:
    for fact in facts:
        pprint(fact["text"])


