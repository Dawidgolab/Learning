"""

JSON - JSON stands for JavaScript Object Notation. It's a lightweight data-interchange format that is easy for humans to read and write,

json.dumps(data) - save data to as a string json
json.dump(data,nameOdFile,ensure_ascii=False) - save data to the file as jason
"""

# How to download the JSON file????

import json #We import the json

film = {
    "title" : "Zrobie to zawsze!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Dawid Gołąb", "Alicja Gołąb"),
    "budget" : None,
    "credits" : {
        "director" : "Dawid Gołąb",
        "writer" : "Barry Cent",
        "animator" : "Calvin Matrix"
    }
}
'''
# dumps (String)
encodedFilm = json.dumps(film,ensure_ascii=False)
print(encodedFilm)


# dump (File)

with open("sample.json",'w',encoding="UTF-8") as file:
    json.dump(film,file,ensure_ascii=False)
'''
###############################################################################
# Loaded
# 1. json.loads(jsonstring) - store jsonstring for data of the phyton type
# 2. json.load(filePointer) - loaded json from file and return as a result of the method data of the phyton type

'''
# 1
encodedRetrievedMovie = '{"title": "Zrobie to zawsze!", "release_year": 1969, "won_oscar": true, "actors": ["Dawid Gołąb", "Alicja Gołąb"], "budget": null, "credits": {"director": "Dawid Gołąb", "writer": "Barry Cent", "animator" : "Calvin Matrix"}}'
decodedMovie = json.loads(encodedRetrievedMovie)
print(decodedMovie)

# 2

with open("sample.json",encoding="UTF-8") as file:
    result = json.load(file) # we changed the json format to phyton format
    print(result)
'''
####################################################################################
# text format
# indent = 4
# sort_keys = True - alphabetical sorting

# indent = 4
encodedFilm1 = json.dumps(film,ensure_ascii=False,indent=4)
print(encodedFilm1)
print("########################################")

# sort_keys = True
encodedFilm2 = json.dumps(film,ensure_ascii=False,indent=4,sort_keys=True)
print(encodedFilm2)

# sorting and formating text into the file
with open("sample.json","w",encoding="UTF-8") as file:
    json.dump(film,file,ensure_ascii=False,indent=4,sort_keys=True)

# new library pprint to format with all these features
print("#################################################")
import pprint

with open("sample.json",encoding="UTF-8") as file:
    result = json.load(file)
pprint.pprint(result)