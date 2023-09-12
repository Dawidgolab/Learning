# default arguments
# a)
'''if we assinged the value to the amaunt then we have a default argument
while we do not assign anything when calling the function then we will be have
assign value as a secound argument '''
import time
'''
def increment(x,amount=1):
    return x + amount

print(increment(2))
print("//////////////")
# b)
num1 = int(input("num1: "))


def add(num1):
    result = [element
              for element in range(1,num1+1)]
    return result

def function_timer(func,arg,how_many_times = 1):
    sum = 0

    for i in  range(0,how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end - start)

    return sum

print(function_timer(add,num1))

def adding(count = 1):
    total = 0
    for i in range(count):
        number = int(input(str(i+1) + " number:"))
        total += number
    return total

counter = int(input("give the number of the count: "))

print(adding(counter))
-------------------------------------------------------------------------
#key and positional arguments with sep - this is a separator which spilts e.g two arguments
def greet(name,message):
    print(message,name,sep=" 888 ")

#POSIITONAL ARGUMENTS are in the function greet(NAME,MESSAGE)
greet("Dawid","Witajcie")

#assigning to the value name = "dawid" message = "Hello"
# allows us to switch the values that are in the definition of the
#!KEY ARGUMENTS
greet(message="hello",name = "alicja")
------------------------------------------------------------
'''
#multivariate arguments
# * [it is very similar to listi mean this is kind of list]- we can send multiple arguments to (values), but they cannot be named(tuple)
# ** -  we can sent many arguments into the (value) but the have to be named(dictionary)
#!! Arguments that are not named must come before the named ones

import time

def check(num1,container):
    if num1 in container:
        return True
    else:
        return False

def time_measure(func, *arg, how_many_times):
    total_time = 0
    print(arg.get("setContainer"))
    for i in range(how_many_times):
        start = time.perf_counter()
        result = func(*arg)
        end = time.perf_counter()
        total_time += (end - start)

    return total_time


#Example list and set
setContainer = {num1
                for num1 in range(1000)}
listContainer = [num2
                 for num2 in range(1000)]

# Mierzymy czas wykonania funkcji checkset
time_checkset = time_measure(check, 103, setContainer, how_many_times=50000)

# Mierzymy czas wykonania funkcji checklist
time_checklist = time_measure(check, 203, listContainer, how_many_times=50000)

print("Czas wykonania checkset:", time_checkset)
print("Czas wykonania checklist:", time_checklist)