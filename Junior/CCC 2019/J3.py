n = int(input())

string = []

for i in range(n):
    lines = input()
    string.append(lines)

for j in range(n):
    count = 0
    message = " "
    k = string[j]

    for i in range(len(k)):
        if i != len(k) - 1 and k[i] == k[i + 1]:
            count += 1
        else:
            message = message + " " + str(count + 1) + " " + k[i]
            encodedMessage = message[2:len(message)]
            count  = 0
    
    print(encodedMessage)
