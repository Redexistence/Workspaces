# Question 2 (Pig Latin)
# Rules:
# 1. If a word starts with a vowel, add 'way' to the end
# 2. If a word starts with a consonant, move the first consonant or consonant cluster to the end and add 'ay'

def pig_latin(word):
    vowels = 'aeiou'
    if word[0] in vowels:
        return word + 'way'
    else:
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + 'ay'
        return word + 'ay'

line = input("Enter word or message: ")
words = line.split()
pig_latin_words = [pig_latin(word) for word in words]
print(' '.join(pig_latin_words))