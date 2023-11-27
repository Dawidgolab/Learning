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


import requests
def serverRespond():
    webName = input("Give the URL adress: ")
    if not webName.startswith('https://') and not webName.startswith('http://'):
        webName = 'https://' + webName

    try:
        web = requests.get(webName)
        status = web.status_code

        if status == 200:
            print(f"This site exists!!!(code - {web.status_code})")
        else:
            print(f"ERROR!!! There is no such page!!!(code - {web.status_code})")
            with open("test.txt",'a+',encoding="UTF-8") as file:
                file.write(webName+"\n")
    except requests.exceptions.RequestException:
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

