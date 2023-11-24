#nested types(typy zagnieżdżone) first [] - respond for up and down
# secoud [] - respond for right and left

ListOfGuests ={
    ('Dawid',29,'man',664773882),
    ('Alicja',45,'woman',772995883),
    ('Kamila',19,'woman',4729375493),
}
ListOfGuests2 ={
    ('Dawid',29,'man'),
    ('Magda',45,'woman'),
    ('Kinga',19,'woman'),
}
'''print(ListOfGuests[1][0])'''
'''
listOfGuests3 = ListOfGuests & ListOfGuests2
print(listOfGuests3)

for name , age, sex, phone in ListOfGuests:
    print('Name: ',name)
    print('Age: ',age)
    print('Sex: ',sex)
    print('Phone number: ', phone)
    print('\n')


'''

people = {
    "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
    "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
    "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
    "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
    "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
    "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
    "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
    "4WW4F4HiUTP5dBdHatPw": {'name': 'Marie', 'age': 2, 'sex': 'Female'},
    "yuHhrXS1xsSql7kIEnUH": {'name': 'Leila', 'age': 24, 'sex': 'Female'},
    "76XBNSkJn1BIRoX3hB0s": {'name': 'Eric', 'age': 27, 'sex': 'Male'},
    "dMii4kQO1XW4WoiVI7S4": {'name': 'Tobey', 'age': 22, 'sex': 'Female'},
    "DU3Zi0aNj2LLAfujLUWB": {'name': 'Missy', 'age': 25, 'sex': 'Female'}
}

'''for firstkey in people:
    print("ID:",firstkey)
    for secoundarykey in people[firstkey]:
        print(secoundarykey,people[firstkey][secoundarykey])'''
'''
1. w slowniku people wyswietl pierwszy klucz 
2. dla vartosci w slowniku ktory jest 'pierwszym kluczem' w 'people'
czyli wchodzimy do głównego slownika ktory ma wewnatrz slownika i chcemy z niego 
odczytac slowniki z wartosciami.
'''

people2 = [
    {'id:': 'IcFDG2bO9AYDF651DoyH', 'name:': 'John', 'age:': 27, 'sex:': 'Male'},
    {'id:': 'KcD9ntE6IRM59vkVta1k', 'name:': 'Marie', 'age:': 22, 'sex:': 'Female'},
    {'id:': 'yDlgcn99xPc19mYXcRmy', 'name:': 'Agness', 'age:': 25, 'sex:': 'Female'}
]
'''
for slownik in people2:
    for key in slownik:
        print(key,slownik[key])

1. dla kazdego slownika w  people , ponizsza petla wykona sie 3 razy
2. dla kazdego key w slowniku(key = id , name, age...)
3.wypisuj klucze i wartosci(czyli klucze w danym 'slowniku ')
'''

people3 = [
    "Arkadiusz",
    "Wiola",
    "Kuba"
]

oceny = {
    "Arkadiusz": (2,1,2,3,2,3),
    "Wiola": (4,2,1,3,4)
}





ratings1 = {
            "Arkadiusz":(2,4,6,3,1,3),
            "Agness": (4,3,5,6,4)
           }

ratings2 = [
    {'name': "Arkadiusz", 'ratings': (2, 4, 6, 3, 1, 3), 'behavior': 4},
    {'name': "Agness", 'ratings': (4,3,5,6,4), 'behavior': 2}
]

ratings3 = {
    "Arkadiusz": {'ratings': (2, 4, 6, 3, 1, 3), 'behavior': 4},
    "Agness": { 'ratings': (4,3,5,6,4), 'behavior': 2}
}
'''
for data in ratings1:
    print(data,ratings1[data])

'''

print(people.items())

for id, dictionary in people.items():
    print('ID :',id)
    for key in dictionary:
        print(key ,':', dictionary[key])



