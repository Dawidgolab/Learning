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

# dumps (String)
encodedFilm = json.dumps(film,ensure_ascii=False)
print(encodedFilm)


# dump (File)

with open("sample.json",'w',encoding="UTF-8") as file:
    json.dump(film,file,ensure_ascii=False)

###############################################################################
"""
{  
   "title":"Ale ja nie będę tego robił!",
   "release_year":1969,
   "won_oscar":true,
   "actors":[  
      "Arkadiusz Włodarczyk",
      "Wiolleta Włodarczyk"
   ],
   "budget":null,
   "credits":{  
      "director":"Arkadiusz Włodarczyk",
      "writer":"Alan Burger",
      "animator":"Anime Animatrix"
   }
}
"""