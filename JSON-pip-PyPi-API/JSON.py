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
'''encodedFilm1 = json.dumps(film,ensure_ascii=False,indent=4)
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
'''
#########################################################################################################
# JSONplaceholder - alternate site for you future json
'''import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(r.text)

#tasks = json.loads(r.text)
try:
    tasks = r.json()
    print(tasks[0])
except json.decoder.JSONDecodeError:
    print("Error - there is no jason format!!!")
else:
    print("Everything is fine")
    '''
###########################################################################################################
# Data Processing - this is task where we want to store the data from json file and select the usersID where "completed" = true and count this 'true'
import json
import requests

"""
1:11
2:8 
3:10

10:
"""


r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    taskFrequencyByUser = {}
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                taskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                taskFrequencyByUser[entry["userId"]] = 1
    return taskFrequencyByUser

def get_user_with_top_completed_tasks(taskFrequencyByUser):
    userIdWithMaxCompletedAmountTask = []
    maxAmountOfCompletedTasks = max(taskFrequencyByUser.values())
    for userId, numberOfCompletedTasks in taskFrequencyByUser.items(): # items add us the tuple to easier sort
        if (numberOfCompletedTasks == maxAmountOfCompletedTasks):
            userIdWithMaxCompletedAmountTask.append(userId)
    return  userIdWithMaxCompletedAmountTask




try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Error - there is no jason format!!!")
else:# This is the place where we can proccesing data (we can write it after exept!!!!)
    taskFrequencyByUser = count_task_frequency(tasks)
    userWithTopCompletedTasks = get_user_with_top_completed_tasks(taskFrequencyByUser)

# Continue the task from other website(work on users)
# 1 way

'''
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()

for user in users:
    if (user["id"] in userWithTopCompletedTasks):
        print(f"The winners are users: {user['name']} ")
        userWithTopCompletedTasks.remove(user["id"])

# 2 way

'''

'''
for userId in userWithTopCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/" + str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users/" , params="id=" + str(userId)) # We connect with users - we provide parameters
    user = r.json()
    #print(f"The winners are users: {user['name']} ")
    print(f"The winners are users: {user[0]['name']} ")
'''

# 3 way - download 2 records at the same time

def change_list_into_conj_of_param(my_list,key="id"):
    conj_param = key + "="
    lastIterationNumber = len(my_list)
    i = 0

    for item in my_list:
        i += 1
        if (i == lastIterationNumber):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key +"="

    return conj_param



conj_param = change_list_into_conj_of_param(userWithTopCompletedTasks)
#conj_param = change_list_into_conj_of_param([1,2,3])


r = requests.get("https://jsonplaceholder.typicode.com/users/" , params=conj_param) # We connect with users - we provide parameters

users = r.json()
for user in users:
    print(f"The winner is : {user['name']}")

