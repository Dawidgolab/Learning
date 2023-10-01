file_name = "test.txt"

# Wczytanie istniejącej zawartości pliku (jeśli istnieje)
try:
    with open(file_name, "r") as plik:
        istniejacy_tekst = plik.read()
except FileNotFoundError:
    istniejacy_tekst = ""

while True:
    # Wyświetlenie istniejącej zawartości
    print("Aktualna zawartość pliku:")
    print(istniejacy_tekst)

    # Menu użytkownika
    print("Co chcesz zrobić?")
    print("1. Dodaj tekst")
    print("2. Usuń tekst")
    print("3. Wyjdź z programu\n")

    wybor = input("Wybierz opcję (1/2/3): ")

    if wybor == '1':
        # Wprowadzenie nowego tekstu od użytkownika
        nowy_tekst = input("Podaj nowy tekst: ")
        istniejacy_tekst += nowy_tekst + "\n"

        # Zapisanie aktualnej zawartości do pliku
        with open(file_name, "w") as plik:
            plik.write(istniejacy_tekst)
    elif wybor == '2':
        # Wprowadzenie tekstu do usunięcia od użytkownika
        tekst_do_usuniecia = input("Podaj tekst do usunięcia: ")
        istniejacy_tekst = istniejacy_tekst.replace(tekst_do_usuniecia + "\n", "")

        # Zapisanie aktualnej zawartości do pliku
        with open(file_name, "w") as plik:
            plik.write(istniejacy_tekst)
    elif wybor == '3':
        # Zakończenie programu
        print("Koniec programu.\n")
        break
    else:
        print("Nieprawidłowy wybór. Wybierz opcję 1, 2 lub 3.")

# Wyświetlenie całej zawartości pliku po zakończeniu programu
with open(file_name, "r") as plik:
    zawartosc_po_zakonczeniu = plik.read()

print("Zawartość pliku po zakończeniu programu:")
print(zawartosc_po_zakonczeniu)

'''Ważne Informacje !!!'''

# WITH
# with: To słowo kluczowe używane do otwierania pliku w sposób bezpieczny,
# zapewnia automatyczne zamknięcie pliku po zakończeniu pracy.


