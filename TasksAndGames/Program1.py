'''
Napisz program , który pozwoli użytkownikowi:
1) Dodawać nowe definicje(key and description - używamy słownika)
2) Szukać istniejących definicji
3) Usuwać wybrane przez niego definicje
'''

definitions = {}
print("Witamy w programie Definicji!!! Wybierz opcje od 1 do 4!!! \n ")
while True:
    print("1 - Dodaj nową definicje")
    print("2 - Wyszukaj istniejącą definicje")
    print("3 - Usuń istniejącą definicje")
    print("4 - Zakończ program")

    chose = input("Co chcesz zrobić: \n")
    if chose == '1':
        key = input("Podaj klucz: \n")
        definition = input("Podaj definicje do klucza: \n")
        definitions[key] = definition
        print("Dodano poprawnie definicje!!!\n")
    elif chose == '2':
        key = input("Podaj klucz/nazwe którą chcesz wyszukać: \n")
        if key in definitions:
            print(definitions[key])
        else:
            print("Nie ma takiej definicji!!!\n")
    elif chose == '3':
        key = input("Podaj klucz/nazwe którą chcesz usunąć: \n")
        if key in definitions:
            del definitions[key]
            print("Usunięto",key,"poprawnie!!!\n")
        else:
            print("Nie ma takiej definicji do usunięcia\n")
    elif chose == '4':
        print("Dziękuje za skorzystanie z mojego programu do definicji!!! Dozobaczenia!!!!")
        break
    else:
        print("Wpisałeś złą opcje , spróbuj jeszcze raz\n")




