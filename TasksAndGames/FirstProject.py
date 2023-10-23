from enum import IntEnum
print("Welcome to the List of guests!!!\n")

ListGuests = []

while True:
    menu = IntEnum('Menu','AddGuest DelGuest SearchGuest ShowAll ')
    choice = int(input(
"""Choose an option: 
1 - add member
2 - delete member
3 - search member
4 - display the all members
5 - exit
"""))

    if choice == menu.AddGuest:
        name = input("Give the name: \n")
        ListGuests.append(name)
        print("Adding '" + name + "' succeeded!!!\n")

    elif choice == menu.DelGuest:
        name = input("Specify the member you want to remove: \n")
        if name in ListGuests:
            ListGuests.remove(name)
            print("Removing succeeded!!!\n")
        else:
            print("The specified member is not in the list!!!\n")

    elif choice == menu.SearchGuest:
        name = input("Specify the member you want to search: ")
        for member in ListGuests:
            if name in ListGuests:
                print("Member found:",name)
                break
        else:
            print("Member not found in the list!!!\n")

    elif choice == menu.ShowAll:
        print("List of all members:")
        for member in ListGuests:
            print(member)
        print("\n")

    elif choice == '5':
        print("Goodbye\n")
        break

    else:
        print("You have chosen the wrong option, try again!!!\n")
