import sys
from collections import deque

def solve():
    # Use fast I/O for large grid inputs
    input = sys.stdin.read().split()
    if not input: return
    
    M = int(input[0])
    N = int(input[1])
    
    # Pre-map products to the values found at those coordinates
    # adj[product] will store values found at cells (r, c) where r*c = product
    adj = {}
    
    idx = 2
    for r in range(1, M + 1):
        for c in range(1, N + 1):
            val = int(input[idx])
            product = r * c
            if product not in adj:
                adj[product] = []
            adj[product].append(val)
            idx += 1

    # Start BFS from the starting cell (1, 1). Its value determines where we jump.
    # We want to know if we can reach a cell whose product is M * N.
    target_product = M * N
    start_value = int(input[2]) # Value at (1, 1)
    
    queue = deque([start_value])
    visited = {start_value} # Use a set for O(1) lookups to avoid TLE

    while queue:
        current_val = queue.popleft()
        
        # If current cell value matches the exit's coordinates (M*N), we can escape
        if current_val == target_product:
            print("yes")
            return

        # Check all cells we can reach based on this product
        if current_val in adj:
            for next_val in adj[current_val]:
                if next_val not in visited:
                    visited.add(next_val)
                    queue.append(next_val)

    print("no")

solve()
