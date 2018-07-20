# Numpy arrays are an alternative to Python lists
# They are fast and easy to work with
import numpy as np

# we don't know what numpy does so maybe we want to look up a function
#print(dir(np))
#print(help(np.hamming))

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# let's calculate BMI
bmi = np_weight / np_height ** 2
print(bmi)
print("")
print("A subset allows you to only grab the elements of the array that match a clause"
print(bmi > 23)
print(bmi[bmi > 23])
