books = input().strip()
nL = books.count('L')
nM = books.count('M')
nS = books.count('S')

L_sec = books[:nL] # Large section
M_sec = books[nL:nL+nM] # Medium section
S_sec = books[nL+nM:] # Small section

L_in_M = M_sec.count('L')
L_in_S = S_sec.count('L')
M_in_L = L_sec.count('M')
M_in_S = S_sec.count('M')
S_in_L = L_sec.count('S')
S_in_M = M_sec.count('S')

swap_L_M = min(M_in_L, L_in_M)
swap_L_S = min(S_in_L, L_in_S)
swap_M_S = min(S_in_M, M_in_S)

rem_M_in_L = M_in_L - swap_L_M
rem_L_in_M = L_in_M - swap_L_M
rem_S_in_L = S_in_L - swap_L_S
rem_L_in_S = L_in_S - swap_L_S
rem_S_in_M = S_in_M - swap_M_S
rem_M_in_S = M_in_S - swap_M_S

cycles = rem_M_in_L + rem_S_in_L
min_swaps = swap_L_M + swap_L_S + swap_M_S + 2 * cycles

print(min_swaps)