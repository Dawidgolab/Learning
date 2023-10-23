#module - it's a file with code . it is an element to be used
# as part of something bigger
# there are three modules:
'''
1. standards libraries
2. we can installed from various sources
3. the last one is the module which we write ourselves
'''
# To take adventage of other file we need to import as library the name of the file
from TasksAndGames import Figure

while True:
    print("""Select the figure whose area you want to calculate
1. Square
2. Rectangle
3. Circle 
4. Triangle
5. Trapezoid 
""")

    choice = input("Choose the option: \n")

    if choice == '1':
        a = int(input("give the number a:"))
        print("Area of square is", Figure.pole_kwadratu(a), "\n")

    elif choice == '2':
        a = int(input("give the number a:"))
        b = int(input("give the number b:"))
        print("Area of rectangle is", Figure.pole_prostokata(a, b), "\n")

    elif choice == '3':
        r = int(input("give the radian r:"))
        print("Area of circle is", Figure.pole_kola(r), "\n")

    elif choice == '4':
        a = int(input("give the number b:"))
        h = int(input("give the number h:"))
        print("Area of triangle is", Figure.pole_trojkata(a, h), "\n")

    elif choice == '5':
        a = int(input("give the number a:"))
        b = int(input("give the number b:"))
        h = int(input("give the number h:"))
        print("Area of trapezoid is", Figure.pole_trapezu(a, b, h), "\n")

    elif choice == '6':
        print("bye")
        break

    else:
        print("Wrong options!!!")

# enumeration



