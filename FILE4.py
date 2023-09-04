#Wyrażenie this is a formula for creating dictionaries from already created lists

#wyrażenia i formuły listowe| transformacja listy
''' kiedy potrzebujemy funkcjonalności list
potrzebujemy dodawania list sortowania itp
chcemy wykonac na raz różne operacje na listach
np wyswietlamy lkiczby a pozniej chcemy wyswietlic ich sume
w generatorze uda nam sie tylko i wyłącznie raz wyświetlic pierwszą rzecz
'''
liczby = [1,2,3,4,5,6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)
    print(potegiDwojki)

print()

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)

#wyrażenie listowne 1 górny przyklad
'''
[1. co robimy na elemencie  2. skad wybieramy  3. jakie elementy dokladnie wybieramy]
'''
potegiDwojki2 = [element ** 2
                 for element in range(20) # lub to co na górze do 'liczby'
                 ]
print(potegiDwojki2)

#wyrazenie listowne 2 gorny przyklad

liczbyParzyste2 = [element
                   for element in liczby
                   if element % 2 ==0
                   ]
print(liczbyParzyste2)

liczba = [1,2,3,4,5]

Parzyste = [number
            for number in liczba
            if number % 2 == 0]

print(Parzyste)
print("\n \n //////////////////////////////////////////////////////")






# Wyrażenia generujące
# uzywamy kiedy dane są ogromne i nie potrzebujemny przechowytwac danych
# Generator obiektu który pozwala wyciagać elementy na bieżąco
# () zajmuje duzo mniej pamieci niz []
#!lepiej używać go tylko wtedy kiedy chce się wypisać elementy!
import sys

evenNumbers = [i
               for i in range(10)
               if (i % 2 == 0)
               ]
print(evenNumbers)

evenNumbersGenerator = (i
               for i in range(100)
               if (i % 2 == 0)
                        )
print(sum(evenNumbersGenerator))
print(sys.getsizeof(evenNumbers)) # sprawdza rozmiar getsizeof
print(sys.getsizeof(evenNumbersGenerator))

for i in evenNumbersGenerator:
    print(i)
print("////////////////////////////////////////////////// \n \n \n ")




# Wyrażenia słownikowe (do każdego klucza dopisujemy wartość słownikową)
names = ["Arkadiusz","Wioletta","Karol","Bartłomiej","Jakub","Ania"]
numbers = [1, 2, 3, 4, 5, 6]
celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}



faranheit = {
    label : (far * 9/5) + 36
    for label,far in celcius.items()
}
print(faranheit)


print("/////")

namesLength = {
    name : len(name) #podajemy tutaj co ma się stać z kluczem i wartością
    for name in names # skąd
    if name.startswith('A') #warunek
}
print(namesLength)


multipliedNumbers = {
    number : number * number
    for number in numbers
}

print(multipliedNumbers)

#wyrazenia zbioru

names = {"Dawid", "Wioletta", "Karol", "bartek"}

names = {
    name.capitalize() # Co mamy zrobic z danymi
    for name in names # skad mamy wybrac dane
}
print(names)
