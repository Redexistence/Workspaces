import math
import os

class FormulaError(Exception):
    pass

def edit_input(user_input):
    parts = user_input.split()
    
    if len(parts) == 3:
        num_1, operator, num_2 = parts
        try:
            num_1 = float(num_1)
            num_2 = float(num_2)
        except ValueError:
            raise FormulaError("The first and third input must be numbers.")
        
        if operator not in ('+', '-', '*', '/', '**'):
            raise FormulaError("The second input must be a valid operator (+, -, *, /, **).")
        
        return num_1, operator, num_2
    
    elif len(parts) == 2:
        operator, num_1 = parts
        try:
            num_1 = float(num_1)
        except ValueError:
            raise FormulaError("Second input must be number.")
        
        if operator != 'sqrt':
            raise FormulaError("For two-part formulas, the operator must be 'sqrt'.")
        if num_1 < 0:
            raise FormulaError("Cannot take the square root of a negative number.")

        return num_1, operator, None  # Sqrt does not need num_2

    else:
        raise FormulaError("Neither two or three elements.")

def calculate(num_1, operator, num_2):
    if operator == '+':
        return num_1 + num_2
    elif operator == '-':
        return num_1 - num_2
    elif operator == '*':
        return num_1 * num_2
    elif operator == '/':
        if num_2 == 0:
            raise FormulaError("Cannot divide by zero.")
        return num_1 / num_2
    elif operator == '**':
        return num_1 ** num_2
    elif operator == 'sqrt':
        return math.sqrt(num_1)

while True:
    user_input = input("Enter a formula (e.g., '10 + 5', 'sqrt 25', or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        os.system('cls')
        break
    try:
        parts = edit_input(user_input)
        if len(parts) == 3:
            num_1, operator, num_2 = parts
            result = calculate(num_1, operator, num_2)
        else:
            num_1, operator, _ = parts
            result = calculate(num_1, operator, None)
        print(f"Result: {result}")
    except FormulaError as error:
        print(f"Error: {error}")