# Canadian Postal Code Province and Address Type Finder

province_codes = {
    'A': 'Newfoundland and Labrador',
    'B': 'Nova Scotia',
    'C': 'Prince Edward Island',
    'E': 'New Brunswick',
    'G': 'Quebec',
    'H': 'Quebec',
    'J': 'Quebec',
    'K': 'Ontario',
    'L': 'Ontario',
    'M': 'Ontario',
    'N': 'Ontario',
    'P': 'Ontario',
    'R': 'Manitoba',
    'S': 'Saskatchewan',
    'T': 'Alberta',
    'V': 'British Columbia',
    'X': 'Nunavut or Northwest Territories',
    'Y': 'Yukon'
}

postal_code = input("Enter postal code: ").strip().upper()

if len(postal_code) < 1 or not postal_code[0].isalpha():
    print("Error: Postal code must start with a letter.")
else:
    first_char = postal_code[0]
    if first_char not in province_codes:
        print("Error: Invalid postal code start value.")
    else:
        province = province_codes[first_char]
        # It is urban if second character is a digit and not 0, rural if 0
        if len(postal_code) > 1 and postal_code[1].isdigit():
            if postal_code[1] == '0':
                address_type = "rural"
            else:
                address_type = "urban"
            print(f"The postal code is for a {address_type} address in {province}.")
        else:
            print("Error: Invalid code format.")