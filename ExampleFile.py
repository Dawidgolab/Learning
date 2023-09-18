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
'''
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

result = matrix[0][0] * matrix[1][1] * matrix[2][2] + \
          matrix[1][0] * matrix[2][1] * matrix[0][2] + \
          matrix[2][0] * matrix[0][1] * matrix[1][2] - \
          matrix[0][2] * matrix[1][1] * matrix[2][0] - \
          matrix[1][2] * matrix[2][1] * matrix[0][0] - \
          matrix[2][2] * matrix[0][1] * matrix[1][0]

print(result)
'''

