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

-> endpoint in api - the place where we can download the something and make additional
query parameters

"""

# task 1 -> download json from stackoverflow by means of API from stackexchange
'''
What we want to download:
1. We want to questions with min 15 points votes
2. sort descending 
3. from last 2 months 
4. category python 
5. prove that is only python with "tags"
6. with using the webbrowser open all this pages which they have all these tags 
'''

"""
import requests
import json
import pprint
import webbrowser
from datetime import datetime , timedelta # timedelta is like minus


# time stamp - sign of the times
# from 1 january 1970 we count how many seconds have passed since then

timeBefore = timedelta(weeks=8)

searchTime = datetime.today() - timeBefore



params = {
    "site": "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : int(searchTime.timestamp()),
    "tagged" : "python",
    "min" : 15
}

r = requests.get("https://api.stackexchange.com/2.3/questions/", params)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format!!!")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])

"""
"""
API KEY allows us for authorizaition(you its you
-> connetion throught the header is more saver  


import requests
import json
import webbrowser

from pprint import pprint



params = {
    "api_key" : "?",
    "country" : "pl",
    "year" : 2023,
    "type" : "national"
}

r = requests.get("https://calendarific.com/api/v2/holidays",params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    pprint(content)
"""

# -> connetion throught the header is more saver(Header - additional information which we can add to request)
# live_EAP8fbe0T2he4TySQAFCG5umfvt4cp9S3Tp0E5dlj8bapHjuJx3y3a3rRgbHUIW1

'''import requests
import json
import webbrowser
from pprint import pprint
import Sensitivedata.credentials


r = requests.get(" https://api.thecatapi.com/v1/favourites/",headers=Sensitivedata.credentials.headers)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    pprint(content)


'''
#user logs in and  gives the password
'''
login = 'dawid'
password = 123
'''
#than we check that login and password is correct which is into the data base
#we assume that the login went through correctly

#we download form data base the userid and name - name or nick of the user

# we need to write the userId and name in data base

# after logging in we want to show the user what their favorite cats are using
# our catAPI

# we want to show him the posibilities about the adding
# a new cats(THE RANDOM CATS so if he wants to add then he will add )
# and we allow him to remove the cat form FAVOURITE CATS

import requests
import json
import webbrowser
from pprint import pprint
import Sensitivedata.credentials


def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Invalid format",response.text)
    else:
            return content


def get_favourite_cats(userId):
    params = {
        "sub_id" : userId
    }
    r = requests.get(" https://api.thecatapi.com/v1/favourites/", params, headers=Sensitivedata.credentials.headers)
    return get_json_content_from_response(r)

def get_random_cat():

    r = requests.get(" https://api.thecatapi.com/v1/images/search",
                     headers=Sensitivedata.credentials.headers)

    return get_json_content_from_response(r)


def add_favourite_cat(catId, userId):
    catData = {
        "image_id" : catId,
        "sub_id" : userId
     }
    r = requests.post(" https://api.thecatapi.com/v1/favourites/",
        json = catData,  headers=Sensitivedata.credentials.headers)

    return get_json_content_from_response(r)




userId = "daw2g4"
name = "Dawid"

favouriteCats = get_favourite_cats(userId)
randomCat = get_random_cat()

print("Give your login and password :")
print("Welcome "+ name + "\n")

if favouriteCats:
    for counter,cat in enumerate(favouriteCats,start=1):
        print(counter,"my favourite cat -> " , cat["image"]["url"])
print("\n\n")

print("Wait ... I generate a random cat... ", randomCat[0]["url"],"\n")


addToFavourites = input("Do you wanna add it to favorites? (T/N)\n")

if(addToFavourites.upper() == 'T'):
    print(add_favourite_cat(randomCat[0]["id"],userId))
else:
    print("Ok, bye!!!")
