# import a module
import re


# Set a variable that holds the list of functions from the module
myls = dir(re)
# Initalise an Array
foundmods = []
for each in myls:
    if "find" in each: # if string "find" is found in the name of the module
        foundmods.append(each) #append the module name to a list

print(sorted(foundmods)) # sort and print the list of modules that contain the string "find"
