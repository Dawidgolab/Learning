#Lambda - we can use it instead of short functions

#0 This is a function where we can write in a 'lambda' manner. Like i said short function
def podwoj(x):
    return x * 2
print(podwoj(3))

#1 lambda multiplication
test = lambda x: x * 2
print(test(3))

#2 lambda where x equal to 5
print((lambda x: x*2)(5))

#3 lambda modulo
my_list = [1,2,3,4,5,6,7,8,9,22,4532,654,3124,67457]
even_number = list(filter(lambda x: x % 2 == 0, my_list))

print(even_number)
