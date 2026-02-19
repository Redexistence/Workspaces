from collections import defaultdict

def read_rules():
    rules = defaultdict(list)
    for _ in range(int(input())):
        s1, s2 = input().split()
        rules[s1].append(s2)
    return rules

must = read_rules()
must_not = read_rules()

violations = 0
for _ in range(int(input())):
    group = set(input().split())
    for i in group:
        violations += sum(mi not in group for mi in must.get(i, []))
        violations += sum(mni in group for mni in must_not.get(i, []))

print(violations)