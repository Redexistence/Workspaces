# VERSION 1 (15/30)
wordsrc = []
worddst = []

for i in range(3):
    rss = input().split()
    wordsrc.append(rss[0])
    worddst.append(rss[1])

ss = input().split()
steps = int(ss[0])
src = ss[1]
dst = ss[2]

def replace(word, x, rn):
    list1 = []
    for i in range(len(word)):
        cpos = i
        j = 0
        while j < len(x) and cpos < len(word) and word[cpos] == x[j]:
            cpos += 1
            j += 1
        if j == len(x):
            newword = word[0:i] + worddst[rn] + word[cpos:]
            list1.append([rn+1, i+1, newword])
    return list1

visited = {}

def getdststring(cur, curstep, records):
    if curstep > steps:
        return False
    if curstep == steps:
        if cur == dst:
            for x in records:
                print(x[0], x[1], x[2])
            return True
        return False
    
    state = (cur, curstep)
    if state in visited:
        return False
    visited[state] = True
    
    for i in range(3):
        thelist = replace(cur, wordsrc[i], i)
        for y in thelist:
            records.append(y)
            if getdststring(y[2], curstep+1, records):
                return True
            records.pop()
    
    return False

getdststring(src, 0, [])

"""
# VERSION 2 (Still 15/30)
from collections import deque

wordsrc = []
worddst = []

for _ in range(3):
    a, b = input().split()
    wordsrc.append(a)
    worddst.append(b)

steps, src, dst = input().split()
steps = int(steps)

# Precompute max possible length change
max_delta = max(abs(len(worddst[i]) - len(wordsrc[i])) for i in range(3))

def generate(word):
    results = []
    for i in range(3):
        start = 0
        while True:
            pos = word.find(wordsrc[i], start)
            if pos == -1:
                break
            new_word = (
                word[:pos] +
                worddst[i] +
                word[pos + len(wordsrc[i]):]
            )
            results.append((i + 1, pos + 1, new_word))
            start = pos + 1
    return results

queue = deque()
queue.append((src, 0, []))
visited = set()

while queue:
    cur, step, path = queue.popleft()

    if step == steps:
        if cur == dst:
            for p in path:
                print(*p)
            break
        continue

    state = (cur, step)
    if state in visited:
        continue
    visited.add(state)

    # Length pruning
    if abs(len(cur) - len(dst)) > (steps - step) * max_delta:
        continue

    for rule, pos, nxt in generate(cur):
        queue.append((
            nxt,
            step + 1,
            path + [(rule, pos, nxt)]
        ))
"""