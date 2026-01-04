dusa_size = int(input())
while True:
    yobi_size = int(input())
    if yobi_size < dusa_size:
        dusa_size += yobi_size
    else:
        break
print(dusa_size)