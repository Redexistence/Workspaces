plate_num = input("license plate num: ").strip()

def is_old_style(plate):
    return len(plate) == 6 and plate[:3].isalpha() and plate[:3].isupper() and plate[3:].isdigit()

def is_new_style(plate):
    return len(plate) == 7 and plate[:4].isdigit() and plate[4:].isalpha() and plate[4:].isupper()

if is_old_style(plate_num):
    print("The license plate is valid for the older style (three letters followed by three numbers).")
elif is_new_style(plate_num):
    print("The license plate is valid for the newer style (four numbers followed by three letters).")
else:
    print("The license plate is not valid for either style.")