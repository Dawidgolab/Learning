#Lambda - we use it for short functions
def podwoj(x):
    return x * 2

print(podwoj(3))

#1 lambda
test = lambda x: x * 2
print(test(3))

#2 lambda
print((lambda x: x*2)(4))



my_list = [2,5,7,33,55,22,11,66,34]

my_list_filtered = list(filter(lambda x: x % 2 == 0,my_list))
print(my_list_filtered)