def unique_characters(input_string):
    unique_chars = set(input_string)
    return len(unique_chars)

user_input = input("Enter a string: ")
unique_count = unique_characters(user_input)
print(f"unique characters: {unique_count}")