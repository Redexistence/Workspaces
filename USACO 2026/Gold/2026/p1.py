import sys

sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    
    A = [int(x) - 1 for x in data[1:N+1]]
    
    M = int(data[N+1])
    
    queries = []
    idx = N + 2
    for _ in range(M):
        ci = int(data[idx]) - 1
        vi = data[idx+1]
        queries.append((ci, vi))
        idx += 2

    current_type = [None] * N
    first_night = [float('inf')] * N
    prev_type_of_query = [None] * M
    
    for i in range(M):
        c, v = queries[i]
        prev_type_of_query[i] = current_type[c]
        if current_type[c] is None and first_night[c] == float('inf'):
            first_night[c] = i + 1
        current_type[c] = v

    vis = [0] * N
    is_lb = [False] * N
    for i in range(N):
        if vis[i] == 0:
            curr = i
            path = []
            while curr >= 0 and vis[curr] == 0:
                vis[curr] = 1
                path.append(curr)
                curr = A[curr]
            if curr >= 0 and vis[curr] == 1:
                cycle_start_idx = path.index(curr)
                cycle_nodes = path[cycle_start_idx:]
                min_node = min(cycle_nodes, key=lambda x: first_night[x])
                is_lb[min_node] = True
            for node in path:
                vis[node] = 2

    parent = list(range(N))
    size = [1] * N
    
    def find(i):
        curr = i
        while parent[curr] != curr:
            curr = parent[curr]
        root = curr
        curr = i
        while curr != root:
            nxt = parent[curr]
            parent[curr] = root
            curr = nxt
        return root

    for i in range(N):
        if current_type[i] is None and not is_lb[i]:
            root_u = find(i)
            root_v = find(A[i])
            if root_u != root_v:
                parent[root_u] = root_v
                size[root_v] += size[root_u]

    total = {'C': 0, 'O': 0, 'W': 0}
    for i in range(N):
        if current_type[i] is not None and parent[i] == i:
            total[current_type[i]] += size[i]
            
    ans = []
    for i in range(M - 1, -1, -1):
        ans.append(f"{total['C']} {total['O']} {total['W']}")
        
        c, v = queries[i]
        v_prev = prev_type_of_query[i]
        
        if v_prev is not None:
            total[v] -= size[c]
            total[v_prev] += size[c]
            current_type[c] = v_prev
        else:
            total[v] -= size[c]
            current_type[c] = None
            if not is_lb[c]:
                root_v = find(A[c])
                parent[c] = root_v
                t_v = current_type[root_v]
                if t_v is not None:
                    total[t_v] += size[c]
                size[root_v] += size[c]

    print('\n'.join(reversed(ans)))

if __name__ == '__main__':
    solve()