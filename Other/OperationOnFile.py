#Type of the operations on file:
'''
- opening
- writing/reading
- closing
'''
# How to open the files:
'''
1. r - Reading - default
2. w - Writing - if the file already exists, it will delete it and save a new one ,
 but if it does not exist, a new one will be created
3. a - Append 
'''


'''
file = open("test","w") #Handle
file.write("Sample")
file.close()
'''



'''
try: # we try something
    file = open("test","w") #Handle
    file.write("Sample1")

    print(0/0) # we make the error
    file.write("Sample2") # value after error will not be assigned

# and finally we close the file
finally:
    file.close()
'''


# better way than before when we have an error

'''with open("test","w") as file:
    file.write("Hello!")

    print(0/0)
    file.write("World!!!")'''

# splitlines funtion
'''print("Splitlines funtion ->>>>>\n")

with open("Oceans.txt","r",encoding="UTF-8") as file:
    oceans = file.read().splitlines()
    oceans1 = file.readline()

print(oceans)
print(f"encoding = {file.encoding}\n")
print("----------------------------------------------------------------\n")


# readline funtion
print("Readline funtion ->>>>>\n")

with open("Oceans.txt","r",encoding="UTF-8") as file:
    oceans1 = file.readline()
print(oceans1)
print("----------------------------------------------------------------\n")

# sample with  'for loop'
print("Sample with  'for loop' ->>>>>\n")

with open("Oceans.txt","r",encoding="UTF-8") as file:
    for line in file:
        print(line)
print()
print("----------------------------------------------------------------")'''

# tell and seek functions

print("The 'tell' function tells us exactly where we are.  !!!\n")
with open("Oceans.txt","r",encoding="UTF-8") as file:
    print(f"1.{file.readline()} ---> Function tell: {file.tell()}")
    print(f"2.{file.readline()} ---> Function tell: {file.tell()}\n")
    print(f"We use the 'seek' function to return to the first line : {file.seek(0)}")
    print(f"1.{file.readline()} ---> Function tell: {file.tell()}")

print()
print("----------------------------------------------------------------")
