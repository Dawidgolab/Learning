import Figure

from enum import IntEnum
# Gdy jest samo Enum - to dopisujemy po .value
# Gdy jest IntEnum - to juz tego nie musimy
# mozemy również użyć enuma jako słownika wtedy by wyglądało to :
#   Menu_Figury = IntEnum('Menu_Figures', {'Square': 1 ,'Rectangle':2, 'Circle':3, 'Triangle':4, 'Trapezoid':5})

while True:
    Menu_Figury = IntEnum('Menu_Figures','Square Rectangle Circle Triangle Trapezoid')
    print(list(Menu_Figury))
    choice = int(input(
"""Select the figure whose area you want to calculate
1. Square
2. Rectangle
3. Circle 
4. Triangle
5. Trapezoid 
"""))

    if choice == Menu_Figury.Square :
        a = int(input("give the side of the square :"))
        print("Area of square is",Figure.area_square(a),"\n")

    elif choice == Menu_Figury.Rectangle:
        a = int(input("give the first side of the rectangle"))
        b = int(input("give the secound side of the rectangle:"))
        print("Area of rectangle is",Figure.area_rectangle(a,b),"\n")

    elif choice == Menu_Figury.Circle:
        r = int(input("give the radian of the circle:"))
        print("Area of circle is",Figure.area_circle(r),"\n")

    elif choice == Menu_Figury.Triangle:
        a = int(input("give the side of the triangle:"))
        h = int(input("give the height of the triangle :"))
        print("Area of triangle is",Figure.area_triangle(a,h),"\n")

    elif choice == Menu_Figury.Trapezoid:
        a = int(input("give the lower base of the trapezoid:"))
        b = int(input("give the upper base of the trapezoid:"))
        h = int(input("give the height of the trapezoid :"))
        print("Area of trapezoid is",Figure.area_trapezoid(a,b,h),"\n")

    elif choice == '6':
        print("bye")
        break

    else:
        print("Wrong options!!!")
