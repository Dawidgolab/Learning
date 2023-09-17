#Object - th eobject is a variable
'''
- The dot next to object(variable) shows us the
METHODs(functions) we
we can use with the object
* Equals sign means assigning a new address!!
'''

#immutable(niezmienna) object
# (bool, int, float, tuple, str)
print("""#####Immutable######: 
immerse objects guarantee us that under a will be 4,
even if 7 is assigned to the value of b ####
!!!!!!!Change doesn't occurs on the original !!!!!!!!""")
a = 4
b = a
b = 7
print(a)
print(b,"\n")


#mutable(zmienna)
print("""######Function id returns us the address of objects#####
!!!!!!!Change occurs on the original !!!!!!!!""")
listSample = [1,4,534,23]
print("1 id of 1 list :",id(listSample))
listSample2 = listSample
print("2 id list2 = list1:",id(listSample))
listSample2.append(465)
print("3 id after appending:",id(listSample),"\n")

#"function with checking id"
print("#####Function with checking id#######")
c = 5
print("1 id global variable(object):",id(c))
def add(c, amount = 1):
    print("2 id without adding:",id(c))
    c = c + amount
    # after change the id is also changed
    print("3 id after adding:",id(c))
print("\n")


#List with id
print("####List with id######")
def append_element_to_list(lista,element):
    print("1 id without element:",id(lista))
    lista.append(element)
    print("2 id with element:",id(lista))

print("Main list where we dont use the function:",id(listSample))
append_element_to_list(listSample,5)
print(listSample)