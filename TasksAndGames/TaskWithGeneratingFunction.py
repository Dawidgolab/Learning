# task 1
'''
Create an infinity function that generates consecutive numbers
that are multiplied by themselves:

-> 1
-> 4
-> 9
-> 16
-> 25

Use the 'generating function' to generate 20 elements ,
then return from the end and generate the next 30 numbers . Save these elements in the same list

'''


def multiplied_numb_by_themselves():
    x = 0
    while True:
        x += 1
        yield x * x

def list(multipliedNumbByThemselves,numberOfElements):
    multiplicationList = []
    for numb in range(numberOfElements):
        multiplicationList.append(next(multipliedNumbers))
    return multiplicationList


multipliedNumbers = multiplied_numb_by_themselves()

firstList = list(multipliedNumbers,20)
print("list with 20 elements: ", firstList)

secondList = firstList + list(multipliedNumbers,30)
print("List with 30 elements: ",secondList)
