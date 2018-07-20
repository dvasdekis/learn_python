def my_function():
  print("Hello from the inside")

def my_function_with_args(username, greeting):
  print("Hello, %s, from My_function!, I wish you %s" % (username, greeting))

my_function()
my_function_with_args("Buttos", "Death")

print("Functions can return a value to the caller with the 'return' keyword")
def sum_two_numbers(a,b):
  return a + b

x = sum_two_numbers(5,4)
print(x)
