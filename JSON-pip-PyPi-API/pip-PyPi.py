"""
pip - pip installs packeges
Pypi - Phyton Packege index
To download the library reguests we open the pypi.org


import requests
interia = requests.get("https://www.interia.pl/")
print(interia.status_code)
"""
#task1 - we want to download a page and check if it exists
#if it does not exist, then write these pages in the file and if it exists, then display it 'code 200'


'''import requests
def serverRespond():
    webName = input("Give the URL adress: ") #user input

    try:
        web = requests.get(webName) # URL
        status = web.status_code # website code - 200/404

        if status == 200:
            print(f"This site exists!!!(code - {web.status_code})")
        else:
            print(f"ERROR!!! There is no such page!!!(code - {web.status_code})")
            with open("test.txt",'a+',encoding="UTF-8") as file: #we save the wrong site to the file
                file.write(webName+"\n")
    except (requests.exceptions.RequestException,requests.exceptions.MissingSchema,
            requests.exceptions.ConnectionError): # exception due to lack of http....
        print("ERROR!!! There is no such page!!!(code-404)")
        with open("test.txt",'a+',encoding="UTF-8") as file:
            file.write(webName+"\n")




print("Welcome!!! This program will check if the site exists")
print("-------------------------------------------------------")

while True:
    choice = input("""
1 - Check the page exists and the non-existing page will be added to the 'test' file
2 - Exit program 
Select options: """)

    if choice == '1':
        serverRespond()
        continue
    elif choice == '2':
        print("You have finished checking the pages!!! Bye!!!!")
        break
    else:
        print("Wrong option, try again!!!")
        continue

'''

#task 2
# Imagine that your boss has tasked you with opening 1,500 pages from his text file and filtering them to give him only the ones that work.
# The boss wants you to save the working pages to a text file.
# The boss has not yet sent you the file with the pages. All you know is that you will have to perform this task the next day.