import sys

def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    C = int(input_data[2])
    

    moonies = [0] + [int(x) for x in input_data[3:3+N]]
    

    edges = []
    idx = 3 + N
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        edges.append((u, v))
        idx += 2
        

    MAX_T = 1000
    
    dp = [[-1] * (N + 1) for _ in range(MAX_T + 1)]
    dp[0][1] = 0
    
    max_profit = 0
    
    for t in range(MAX_T):
        for u, v in edges:
            if dp[t][u] != -1:
                dp[t + 1][v] = max(dp[t + 1][v], dp[t][u] + moonies[v])
        
        if dp[t + 1][1] != -1:
            profit = dp[t + 1][1] - C * ((t + 1) ** 2)
            max_profit = max(max_profit, profit)
            
    print(max_profit)

if __name__ == '__main__':
    solve()
