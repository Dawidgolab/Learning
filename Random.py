# Random
'''
random()  0 <= x < 1 or [0,1)

uniform(2.5,10.0)  2.5 <= x < 10.0 or [2.5, 10)

randrange(10)  from the pool (1,2,3,4,5,6,7,8,9)
randrange(0,15,2) - even numbers from the pool (0,2,4 ... 14)

randint(0,4) [from 0, to 4]
'''
import random

#uniform
'''x = 0
while x < 100:
    x = x + 1
    print(random.uniform(0,100))'''

#randrange e.g 1
'''
x = 0

while x <= 10:
    x += 1
    print(random.randrange(10))'''

#randrange with even number e.g 2
'''
x = 0

while x <= 10:
    x += 1
    print(random.randrange(0,10,2))
'''

#randint
'''
for i in range(1,11):
    number = random.randint(0,10)
    print(f"Random number {i}: {number}")
    
'''
