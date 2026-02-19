def longest_palind(word):
    n = len(word)
    if n == 0:
        return 0
    max_len = 1
    palind_tbl = [[False] * n for _ in range(n)]
    for i in range(n):
        palind_tbl[i][i] = True
    for i in range(n-1):
        if word[i] == word[i+1]:
            palind_tbl[i][i+1] = True
            max_len = 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            end_letr = i + length - 1
            if word[i] == word[end_letr] and palind_tbl[i + 1][end_letr - 1]:
                palind_tbl[i][end_letr] = True
                max_len = length
    return max_len

word = input().strip()
print(longest_palind(word))