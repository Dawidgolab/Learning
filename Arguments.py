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

'''import time

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
print("Czas wykonania checklist:", time_checklist)'''
# ** -  we can sent many arguments into the (value) but the have to be named(dictionary)

# #!! Arguments that are not named must come before the named ones
print("!!!!Examples with two stars **!!!!")

print("#1")
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name='John', age=25)
print_kwargs(name='Alice', city='Paris', job='Engineer')
print()


#2
print("#2")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)
print()


#3
print("#3")

def configure_system(**settings):
    for key, value in settings.items():
        print(f"Setting {key} to {value}")

system_settings = {'resolution': '1920x1080', 'volume': 75, 'theme': 'dark'}
configure_system(**system_settings)
print("\n\n\n")





#global range vs local range
# the global function is more important than local
print("Locla and global variable!!!")
def add1():
    c = 5 #This c has local range
    return c

c = 1

print(f"Zmienna lokalna : {add1()}")
print(f"Zmienna globalna:  {c}")

#useing the global value in function but it is not good practise
def add2():
    global a # we have variable a from global range
    a = a + 3
    print(a)

a = 1
add2()

def add3(b,count = 2):
    b = b + count
    print(b)

b = 1
# we are downloading this global b becouse we have two arguments in def add3
add3(b)
print(b)
