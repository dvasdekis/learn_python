age = 23
print(" == is an evaluation function. It checks for equality and returns boolean")
print(age == 23) # prints true
print(age == 3) # prints false

name = "Beavis"
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
else:
    print("I don't know what your name is!")

if name in ['John', 'Beavis']:
    print("It's either John or Beavis")
else:
    print("It isn't John or Beavis!")

print("'is' isn't evaluation of the values of objects. Instead, it checks if the objects themselves are the same object")
x = [1,2,3]
y = [1,2,3]

print("How does (x == y) evaluate? %r" % (x == y))
print("How does (x is y) evaluate? %r" % (x is y))

print("Not before an evaluation just inverts it.")
print("What's not false? %r" % (not(False)))

