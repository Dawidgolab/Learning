#Any and all - functions that check whether there is any(any) value or whether there are all(all) such values

# task1 with my own simple function and then 'any' function, check list whether includes the even number
list1 = [1,3,5,6,7,8]
list2 = [1,3,5,7,9]
list3 = [1,2,3,4,5]


'''def even_numbers(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            return False

    print(f"yes there is a even number like: {even}")

even_numbers(number2)
'''

#any and all

def any_even(list):
    return any([nr % 2 == 0
                for nr in list])

def all_even(list):
    return all([nr % 2 == 0
                for nr in list])



print("list 1 - any:")
if (any_even(list1)):
    print("Yes, there is even number\n")
else:
    print("No , there isn't \n")

print("list 2 - any:")
if (any_even(list2)):
    print("Yes, there is even number\n")
else:
    print("No , there isn't even number \n")

print("list 3 - all:")
if (all_even(list3)):
    print("Yes, there are all even number\n")
else:
    print("No , there aren't even number \n")


# 2
# Use the all() function to specify whether the person has the required skill set.




john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}

jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}

requerd_skills = ['Python','JavaScript' ]

def has_required_skills(person, skills):
    return all([skill in person['skills'] for skill in skills])



print("John:",has_required_skills(john, requerd_skills))
print("Jane:",has_required_skills(jane, requerd_skills))
