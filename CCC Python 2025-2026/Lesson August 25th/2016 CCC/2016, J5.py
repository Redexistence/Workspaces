question = int(input())
n = int(input())
dmojistan = list(map(int, input().split()))
pegland = list(map(int, input().split()))

if question == 1:
    dmojistan.sort()
    pegland.sort()
    total = sum(max(dmo, peg) for dmo, peg in zip(dmojistan, pegland))
else:
    dmojistan.sort()
    pegland.sort(reverse = True)
    total = sum(max(dmo, peg) for dmo, peg in zip(dmojistan, pegland))

print(total)