import sys


s = sys.stdin.readline().strip()
    
current_label = ""
    
i = 0
while i < len(s):
    if s[i] == '+' or s[i] == '-':
        action = "tighten" if s[i] == '+' else "loosen"
            
        i += 1
        num_start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        num = s[num_start:i]
            
        print(f"{current_label} {action} {num}")
            
        current_label = ""
        continue
    else:
        current_label += s[i]
        
    i += 1