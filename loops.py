print("Let's do some loops!")

primes = [2, 3, 5, 7]
for prime in primes:
  print(prime)

# Range() is a function that returns an iterator - a special type, which acts like every number between zero and the input
for each in range(5):
  print(each)

print("give me three until 6, excluding 6")
for each in range(3,6):
  print(each)

print("Give me a range skipping every 2nd")
for each in range(3,8,2):
  print(each)

print("While loops repeat until a condition is met")
count = 0
while count < 5:
  print(count)
  count += 1 # same as count = count + 1

print("Exit a While loop with Break")
mycount = 0
while True:
  print(mycount)
  mycount += 1
  if mycount >= 5:
    break

print("Skip the current block and start the loop again with continue - skip printing even numbers")
for each in range(10):
  #Checking if each is even
  if each % 2 == 0:
    continue
  print(each)


print("Let's use an Else clause to run when a while loop finishes")
count = 0
while (count<5):
  print(count)
  count += 1
else:
  print("Else clause - Count value reached %d" % (count))
print(" ")

print("Let's use the remainder function to break a loop when it hits a limit")
for each in range(1,10):
  if (each%5==0):
    break
  print(each)
else:
  print("You won't see this, as for loop terminates with a break.")
