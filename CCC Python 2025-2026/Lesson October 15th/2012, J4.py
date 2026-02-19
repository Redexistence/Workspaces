K = int(input().strip())
word = input().strip()

out = []
for i, ch in enumerate(word):
    P = i + 1  # positions are 1-based
    S = 3 * P + K # formula given
    # shift back by S within A-Z
    val = (ord(ch) - ord('A') - S) % 26 # wrap-around using modulo
    out.append(chr(val + ord('A'))) # convert back to character

print(''.join(out)) # print the decoded word