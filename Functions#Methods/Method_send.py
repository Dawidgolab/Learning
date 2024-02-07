''' We can use 'send' but we can use first the generator next()
->  if we use the next() after 'send' then it will not work
because the value of next() will be NONE (in this case -> number = yield number * number -> NONE )
number = NONE
after yield = NONE
start number = NONE
AND THE WE HAVE number(NONE) * number(NONE)
!!!! So this is why it will not work !!!!


def multiplied_numb_by_themselves():
    number = 0
    while True:
        print("\n")
        print("Start number: ", number)
        #number += 1 -> this code only add 1 to up
        number = yield number * number
        print("After yield number: ",number)

generatedNumbers = []

numberGenerator = multiplied_numb_by_themselves()
print(next(numberGenerator))
print(numberGenerator.send(20))
print(numberGenerator.send(30))
print(numberGenerator.send(3))

'''

#Improving TaskWithGeneratingFunction

def multiplied_numb_by_themselves():
    x = 0
    while True:
        #x += 1
        x = yield x * x

def list_of_multiplied_numbers(multipliedNumbByThemselves,StartNumberOfElements, EndNumberOfElements):
    multiplicationList = []
    for numb in range(StartNumberOfElements,EndNumberOfElements):
        multiplicationList.append(multipliedNumbers.send(numb))
    return multiplicationList


multipliedNumbers = multiplied_numb_by_themselves()
multipliedNumbers.send(None)

firstList = list_of_multiplied_numbers(multipliedNumbers,1,21)
print("list 1: ", firstList)

secondList = firstList + list_of_multiplied_numbers(multipliedNumbers,30,51)
print("List 2: ",secondList)
