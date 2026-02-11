def decode(n,x):
    print(n*x)

m = int(input())
for i in range(m):
    sr = input().split()
    nn = int(sr[0])
    xx = sr[1]
    decode(nn,xx)