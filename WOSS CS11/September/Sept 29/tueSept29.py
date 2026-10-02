# Input: One last word!
words = input("Input three words on a single line: ")

findIndexSpace = words.find(" ")
word1 = words[0:findIndexSpace]
print("The word %s has the length of %i" % (word1, len(word1)))
words = words[findIndexSpace + 1:]

word2 = words[0:words.find(" ")]
print("The word %s has the length of %i" % (word2, len(word2)))
words = words[words.find(" ") + 1:]

word3 = words # not used because our input suggests a "!" at the end
# get rid of the exclamation mark at the end of the last word
word3 = word3[0:len(word3) - 1]
print("The word %s has the length of %i" % (word3, len(word3)))

myString = "Strings"
# replace index 3 with H
myString = myString[0:3] + "H" + myString[4:]
print(myString)

