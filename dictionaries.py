
print("Dictionaries are an embedded key-value datatype")
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print("Setting values in a dictionary has a new syntax, but it's mostly like setting a variable")
phonebook["James"] = 838477566
phonebook["Jim"] = 838377264
phonebook["Bill"] = 847662781

print(phonebook)
print("")

print("Dictionaries can be iterated over in a loop, but do not keep the order of the values in it")
for name, number in phonebook.items():
  print("Phone number of %s is %d" % (name, number))


print("")
print("Delete a key with del keyword, or pop method")
del phonebook["John"]
phonebook.pop("Bill")
print(phonebook)
