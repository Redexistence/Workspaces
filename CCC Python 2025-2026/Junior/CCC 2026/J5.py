import sys

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit(0)
it = iter(map(int, data))
try:
    N = next(it); L = next(it); Q = next(it)
except StopIteration:
    sys.exit(0)

diff = [0] * (N + 3)
for _ in range(L):
    p = next(it); s = next(it)
    l = max(1, p - s)
    r = min(N, p + s)
    diff[l] += 1
    diff[r + 1] -= 1

covered = [0] * (N + 1)
cur = 0
for i in range(1, N + 1):
    cur += diff[i]
    covered[i] = 1 if cur > 0 else 0

out = []
for _ in range(Q):
    q = next(it)
    out.append('Y' if covered[q] else 'N')

sys.stdout.write("\n".join(out) + ("\n" if out else ""))