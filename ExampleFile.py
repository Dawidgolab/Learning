'''import random

words = []

with open('sowpods.txt','r') as f: #with jest uzywane do obslugi plikow(nazwa , tryb read) jako alias f
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()# oczytujemy linie i stripem usuwamy biale znaki
        # takie jak spacje taby itp a calos jest przypisywana do zmeinnej line
        words.append(line) #dodajemy linie do tablicy words

#generate a random number
random_word = random.randint(0,len(words))

# take the word

print("random word: ", words[random_word])
'''

