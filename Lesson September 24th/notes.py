import re

def process_code_string(s):
    uppercase = ''.join([c for c in s if c.isupper()])
    numbers = map(int, re.findall(r'[+-]?\d+', s))
    total = sum(numbers)
    return f"{uppercase}{total}"

print(process_code_string("abcDEF123xyz-45"))