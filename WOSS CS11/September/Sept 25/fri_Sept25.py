myString = "Univers"
print(myString[6])
print(myString + " " + "ity")
print(myString * 4)
print("\U000026BD" * 5)
print(len(myString))
print(myString[len(myString) - 1])
print(myString[::-1])
print(myString[1:6:3])

myString = "Today class about strings strings strings."
print(myString.count("strings"))
print(myString.find("c"))
indexOfLetter = myString.find("w")
print(indexOfLetter)
myString.replace("strings", "slicing") # does not change because strings are immutable
print(myString)
myString = myString.replace("strings", "slicing") # now it changes because we assigned it to the variable
print(myString)