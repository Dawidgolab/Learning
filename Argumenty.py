# default arguments
# a)
'''if we assinged the value to the amaunt then we have a default argument
while we do not assign anything when calling the function then we will be have
assign value as a secound argument '''
import time

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