x, y, z = map(int, input("Enter three integers separated by spaces: ").split())
# Find maximum of the three numbers using if else (no elif) statements
# if x >= y:
#     if x >= z:
#         max_num = x
#     else:
#         max_num = z
# else:
#     if y >= z:
#         max_num = y
#     else:
#         max_num = z
# print("The maximum number is:", max_num)

# Why do we use elif statements instead of multiple if statements?
# If we use multiple if statements, all the conditions will be checked even if one of the previous conditions is true. This can lead to unnecessary checks and can make the code less efficient. Using elif allows us to check conditions in a mutually exclusive manner, meaning once a condition is met, the rest are skipped, which improves performance and readability.
# Now let's rewrite the code using elif statements for better efficiency and readability.
if x >= y and x >= z:
    max_num = x
elif y >= x and y >= z:
    max_num = y
else:
    max_num = z
print("The maximum number is:", max_num)

def vowels(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:   
        return True
    else:
        return False