#Program with finding time speed
import time

myNum = int(input("give the number:"))

#first way loop
def sum1(myNum):
    sum = 0

    for number in range(1,myNum+1):
        sum +=number

    return sum

#secound way generator
def sum2(myNum):
    return sum([ num for num in range(1,myNum+1)])

#third way Patttern with list(add first and last number , next divide by 2 and multiply by amount of numbers)
list = []
def sum3(myNum):
    for num in range(1,myNum+1):
        list.append(num)
    return (list[0] + list[-1]) /2 * myNum

#fourth way patter where we use the global variable in local variable
num = 4
def sum4():
    global num
    num = 8
    return (1 + num) /2 * num

# finish
def finish(start):
    end = time.perf_counter()
    return end - start

# wywaływanie funkcji funkcją
'''
- first function has an two arguments(the function which we have display and the argument)
- next we create secound function(we assign an one argument and display him )
- in the end of our program we print the function where
first of all write the main function and then inside the main function
we write the name of the secound function with our one argument which we assigned
 in the main fucntion 
'''

def function_timer(func):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return end - start

def show_message(message):
    print(message)


#time1
start = time.perf_counter()
print("result of function 1:",sum1(myNum))
end = time.perf_counter()
print("time of function 1:", finish(start),"\n")

#time2
start = time.perf_counter()
print("result of generator 2:",sum2(myNum))
end = time.perf_counter()
print("time of generator 2:",finish(start),"\n")

#time3 but other way (more profesional)

print("result of Patttern with list 3:",sum3(myNum))

print("time of Patttern with list 3:",end - start,"\n")

#time4

print("result of Patttern 4:", sum4())
print("time of Patttern 4:",function_timer(sum4)  ,"\n")

