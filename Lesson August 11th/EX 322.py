# Tokenizing is the process of converting a string into a list of substrings, known as tokens. In many circumstances, a list of tokens is far easier to work with than the original string because the original string may have irregular spacing.
# Write a fuction that takes a string containing a mathematical expression as its only parameter and breaks it into a list of tokens. Each token should be a parenthesis, an operator, or a number with an optional leading + or - (for simplicity we will only work with integers in this problem.) Return the list of tokens as the function's result.

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        char = expr[i]
        
        if char.isdigit() or (char in '+-' and (i == 0 or expr[i-1] in '()+-*/')):
            num = char
            i += 1
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(num)
            continue
        
        elif char in '+-*/()':
            tokens.append(char)
        
        i += 1
    
    return tokens

expr = input("Enter math expression: ")
tokens = tokenize(expr)
print(tokens)