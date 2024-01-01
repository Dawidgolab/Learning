"""
Public API - application programming interface

* Two samples of API:

Automatic online text translation:
When you use an online text translation application such as Google Translate,
the application uses an API to send the text you want to translate to Google's server.
There, the text is processed and translated, and then a reply with the translated text
is sent back to the app for you to see.

Weather on your phone:
Weather apps on the phone often use weather service APIs. When you open the app,
it sends a query to the server, asking for current weather data for your location.
The server processes the query and returns a response with the weather forecast,
which the app displays on your phone.

"""

# task 1 -> download json from stackoverflow by means of API from stackexchange
'''
What we want to download:
1. We want to questions with min 15 points
2. sort descending 
3. from last week 
4. category python 
'''

import requests
import json
import pprint

params = {
    "site": "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : "2023-11-01",
    "tagged" : "python",
    "min" : 15
}

r = requests.get("https://api.stackexchange.com/2.3/questions/", params)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format!!!")
else:
    pprint.pprint(questions)