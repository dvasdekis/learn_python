import pandas as pd

my_dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]
        }

brics = pd.DataFrame(my_dict)
print(brics)

# add an index (like primary key, but not guaranteed to be unique)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

print("")
print("Print out a single column as a Pandas Series")
print(brics['country'])

print("")
print("Print out columns as a Pandas DataFrame")
print(brics[['country','capital']])

print("")
print("Multiplying two columns together")
print(brics['area'] * brics['population'])

print("")
print("Grab a single row by row number as a pd series")
print(brics.iloc[2])

print("")
print("Grab a single row by row number as a pd dataframe")
print(brics.iloc[[2]])

print("")
print("Grab a single row via the index value (loc)")
print(brics.loc[['IN']])
