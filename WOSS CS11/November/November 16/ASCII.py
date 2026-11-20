def caesar_cipher(text, shift):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if isinstance(shift, bool) or not isinstance(shift, int):
        raise TypeError("shift must be an integer")

    result = ""
    
    for char in text:
        if char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result += chr(shifted)
        elif char.islower():
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted)
        else:
            result += char
            
    return result

text = input("Enter text to encrypt: ")

while True:
    shift_input = input("Enter an integer shift: ").strip()
    try:
        shift = int(shift_input)
        break
    except ValueError:
        print("Invalid shift. Please enter a whole number.")

print(caesar_cipher(text, shift))