'''
Using this generator we can stop the function at the time of our choosing  and it use to generate results in real time!!!
* yield - dostarczyc ,dac
* next()
-> we generate the even numbers one by onewhen we use the YIELD num (this is the function with the element which we want to display)
-> after assigning a function name to a random variable, we use print(next('our function or variable')) to display it
'''
def evenNumbers():
    for num in range(400):
        if num % 2 == 0:
            yield num

a = evenNumbers() # This is the creation of the generating object to save it somewhere and then call it with the next function
print(next(a))
print(next(a))
print(next(a))



print("Another exercise with generating 10 numbers to test this method")

def generate10Numbers():
    x = 0
    while x < 10:
        yield x
        x += 1

tenNumbers = generate10Numbers()

print("-> Generated of full list but we dont assign the variable to this function :",list(generate10Numbers()))

print(next(tenNumbers))
print(next(tenNumbers))
print(next(tenNumbers))
print(next(tenNumbers))























