astring = "Clowns tolday!"
print("The string is '%s'" % astring )
print("There are this many chars: %d" % len(astring))
print("I found the string 'ow' at location %d" % astring.index("ow")) 
print("I found the letter 'l' %d times." % astring.count("l"))
print("This is a slice of the string from index 3 to 7: %s" % astring[3:7])
print("This is a slice from beginning to 7: %s" % astring[:7])
print("This is a slice from 3 to end: %s" % astring[3:])
print("Extended slice syntax looks like [3:7:2] to take every 2nd letter. The output looks like: %s" % astring[3:7:2])
print("To reverse a string, use -1 in extended syntax, like string[::-1]. Output: %s" % astring[::-1])
print("Upper and lower do as you'd expect: "+ astring.upper() + astring.lower())
print("astring.startswith('Clowns'): " + str(astring.startswith("Clowns")))
print("Split with space converts to an array: ")
print(astring.split(" "))