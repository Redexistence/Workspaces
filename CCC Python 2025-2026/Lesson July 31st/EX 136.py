import string

def clean_phrase(phrase):
    return ''.join(
        c.lower() for c in phrase if c.isalnum()
    )

def are_anagrams(phrase1, phrase2):
    return sorted(clean_phrase(phrase1)) == sorted(clean_phrase(phrase2))


sentence_1 = input("1st phrase: ")
sentence_2 = input("2nd phrase: ")

if are_anagrams(sentence_1, sentence_2):
    print("The phrases are anagrams.")
else:
    print("The phrases are not anagrams.")
