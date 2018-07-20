# Classes (in a class)

print("Objects are the encapsulations of variables and functions into a single entity.")
print("Objects get their variables and functions from Classes")
print("Ergo, Classes are a template to create objects with")

class MyClass:
  variable = "blah"
  
  def function(self):
    print("A message in a class")


print("Let's assign the MyClass to an object that we can build on")
myobjectx = MyClass()

print("")
print("Now the variable myobjectx holds an object of the class 'MyClass' that contains the variable and function defined within the class.")
print("So, let's access the variables and functions inside myobjectx")
print(myobjectx.variable)

print("")
print("Now we can change the value of a variable inside an object, which is an instance of a class")
print("Class > Object > Variable")
myobjecty = MyClass()
myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)

print("")
print("To access a function inside an object, use notation similar to accessing a variable")
myobjectx.function()
