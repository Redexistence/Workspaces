import re

def update_product_code(original_code):
    uppercase_letters = ''.join(filter(str.isupper, original_code))
    
    integers = map(int, re.findall(r'-?\d+', original_code))
    
    total_integer = sum(integers)
    
    new_code = f"{uppercase_letters}{total_integer}"
    
    return new_code

def update_all_product_codes(codes):
    return [update_product_code(code) for code in codes]

N = int(input("Enter the number of product codes: "))
original_codes = [input("Enter product code: ") for _ in range(N)]

updated_codes = update_all_product_codes(original_codes)
for code in updated_codes:
    print(code)