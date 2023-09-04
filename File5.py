# def = definition
#def(znacznik funkcji)   NazwaFunkcji(najlepiej nazwa tego co bedzie robić) ():
# jezeli chcemy wywołać funkcje to piszemy NazwaFunkcji()
'''tworzymy funkcje ktora bedzie witała nowo wpisane osoby '''

def Welcome(name):
    print("Welcome",name,"nice to meet you!!!")

Welcome("Dawid")
Welcome("Kinga")

print("//////////////////////////////////////////\n")
#examples
'''
def welcome():
    name = input("enter your name: ")
    print("Welcome",name,"to my program!!!")

welcome()

def welcome2(name):
    print("Welcome",name,"to my program!!!")

welcome2('Martyna')
'''
import figury

# funkcje z wieloma parametrami
'''
(a,b) - in parentheses(nawiasach - parentesis) we specify(określamy) the parameters
To create more than one parameter just give a comma between the arguments
To call a function we write the name of the function, then in parentheses in the same order(w tej samej kolejnosci)
in which we have specified parameters we send the arguments, 
that is, first the value a and then the value b, for example.
'''
def fieldOfTriangle(a,h):
    result = (a * h)
    print("pole trójkąta1 =", result)

'''fieldOfTriangle(3,6)'''
print("///////////////////////////\n")


# return w def - jesteśmy w stanie przypisać do dalszego uzytku (przykłady)

def fieldOfTriangle2(a,h):
    print("pole trójkąta2 =")
    return a * h

print(5 * fieldOfTriangle2(2,5))
########################################################
def dodaj(a,b):
    return a + b

suma = dodaj(2,3)
print(suma)
##################################################
def warunek(x):
    if x > 10:
        return "wieksze niz 10"
    else:
        return "mniejsze lub rowne"
result = warunek(1)
print(result)
##################################################
def calculations(a,b):
    addition = a + b
    subtration = a - b
    return addition,subtration

add,sub = calculations(6,3)
print(add)
print(sub)
##################################################
def evennumb(even):
    if even % 2 == 0:
        return True
    else:
        return False

print(evennumb(4))
print(evennumb(7))