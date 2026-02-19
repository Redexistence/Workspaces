def remove_nums(int_list):
    for i in range(2, len(int_list), 3):
        print(i)
        int_list.pop(i)
    return int_list

# Find the problem:
# In the given list, remove all numbers divisible by 2.
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_nums(int_list))
# Expected output: [1, 3, 5, 7, 9]
# Why there is an issue?
# The issue is that the loop starts from index 2 and removes every third element. However, the length of the list decreases by 1 each time an element is removed.
# How to fix it?
# To fix the issue, we need to decrement the loop counter by 1 after each element is removed.

def remove_nums_fixed(int_list):
    for i in range(2, len(int_list), 3):
        print(i)
        int_list.pop(i)
    return int_list

print(remove_nums_fixed(int_list))