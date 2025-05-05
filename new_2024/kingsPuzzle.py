from itertools import combinations
from collections import defaultdict

def is_connected(n, edges):
    # Check if the graph is connected using BFS/DFS
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(1)  # Start from any node (1 in this case)
    return len(visited) == n

def check_requirements(n, k, edges):
    if not edges:
        return False  # No edges can't satisfy connectivity
    
    # Check no loops and unique edges
    edge_set = set(edges)
    if len(edge_set) != len(edges):
        return False  # Duplicate edges
    if any(u == v for u, v in edges):
        return False  # Self-loops not allowed
    
    dict = defaultdict(lambda: 0)
    for edge in edges:
        temp = tuple(sorted(list(edge)))
        dict[temp] += 1
        if dict[temp] > 1:
            return False
    
    # Check degree distribution
    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    
    distinct_degrees = set(degree[1:])  # Ignore degree[0] as it's a dummy
    if len(distinct_degrees) != k:
        return False
    
    # Check connectivity
    return is_connected(n, edges)

def find_valid_roads(n, k):
    # Generate all possible roads
    all_possible_edges = list(combinations(range(1, n + 1), 2))
    for num_edges in range(n - 1, len(all_possible_edges) + 1):  # Minimum edges for connectivity: n-1
        for edge_set in combinations(all_possible_edges, num_edges):
            if check_requirements(n, k, edge_set):
                return list(edge_set)
    return "IMPOSSIBLE"



def solve(n, k):
    if n == 1:
        print("YES")
        print(0)
        return
    if k >= n:
        print("NO")
        return 
    print("YES")
    ans = []
    if n == 2:
        ans.append("1 2")

    elif k == 1:
        for i in range(1, n):
            ans.append(f"{i} {i+1}")
        ans.append(f"{n} {1}")
    else:
        for i in range(1, k+1):
            last = k + 1
            for j in range(i):
                if last <= i:
                    break
                ans.append(f"{i} {last}")
                last -= 1
        for i in range(k+2, n+1):
            ans.append(f"{k+1} {i}")

    print(len(ans))
    print("\n".join(ans))
    return ans
            


    
n, k = map(int, input().split())
solve(n, k)


# for i in range(500, 501):
#     for j in range(1, i+1):
#         edges = solve(i, j)
#         if edges != None:
#             for temp, edge in enumerate(edges):
#                 edges[temp] = tuple(map(int, edge.split()))
#             # print(i, j, edges, "here")
#             # print(check_requirements(i, j, edges))
#             if check_requirements(i, j, edges) == False:
#                 print("FOund")
#                 print(i, j)
#                 exit()