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


try: # we try something
    file = open("test","w") #Handle
    file.write("Sample1")

    print(0/0) # we make the error
    file.write("Sample2") # value after error will not be assigned

# and finally we close the file
finally:
    file.close()
