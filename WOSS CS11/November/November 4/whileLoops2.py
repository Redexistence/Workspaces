
def displayWords(words: str):
    i = 0
    word = ""
    while i < len(words):
        if words[i].isalpha():
            word += words[i]
        else:
            print(word)
            word = ""
        i += 1
    if word:  # Print the last word if the string doesn't end with a space
        print(word)

count = 1
a = 1
b = 1
while count < 6:
    c = a + b
    print(a)
    a = b
    b = c
    count += 1