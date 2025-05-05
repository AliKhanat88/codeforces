def solve(n, adj):
    
    if n == 2:
        print(2, 2)
        print(1, 1)
        return
    
    dfs = [(1, 0)]
    for v, p in dfs:
        for child in adj[v]:
            if child != p:
                dfs.append((child, v))
    # print(dfs)
    dp = [[[0, 0], [0, 0]] for i in range(n+1)]
    
    for v, p in dfs[::-1]:
        mini_ans_0 = 0
        sumi_ans_0 = 0
        mini_ans_1 = 0
        sumi_ans_1 = 0

        for child in adj[v]:
            if child != p:
                if dp[child][0][0] > dp[child][1][0]:
                    mini_ans_0 += dp[child][0][0]
                    sumi_ans_0 += dp[child][0][1]
                elif dp[child][0][0] < dp[child][1][0]:
                    mini_ans_0 += dp[child][1][0]
                    sumi_ans_0 += dp[child][1][1]
                else:
                    mini_ans_0 += dp[child][0][0]
                    sumi_ans_0 += min(dp[child][1][1], dp[child][0][1])
                mini_ans_1 += dp[child][0][0]
                sumi_ans_1 += (dp[child][0][1])
        dp[v][0] = [mini_ans_0, sumi_ans_0+1]
        dp[v][1] = [mini_ans_1+1, max(1, sumi_ans_1+len(adj[v]))]
    
    if dp[1][0][0] > dp[1][1][0]:
        dfs = [(1, 0, 0)]
    elif dp[1][1][0] > dp[1][0][0]:
        dfs = [(1, 0, 1)]
    else:
        if dp[1][0][1] <= dp[1][1][1]:
            dfs = [(1, 0, 0)]
        else:
            dfs = [(1, 0, 1)]
    ans = [0] * (n+1)
    for v, p, index in dfs:
        if index == 0:
            ans[v] = 1
        else:
            ans[v] = len(adj[v])

        for child in adj[v]:
            if child != p:
                if index == 1:
                    dfs.append((child, v, 0))
                else:
                    if dp[child][0][0] > dp[child][1][0]:
                        dfs += [(child, v, 0)]
                    elif dp[child][1][0] > dp[child][0][0]:
                        dfs += [(child, v, 1)]
                    else:
                        if dp[child][0][1] <= dp[child][1][1]:
                            dfs += [(child, v, 0)]
                        else:
                            dfs += [(child, v, 1)]
    # print(dp)
    print(dp[1][dfs[0][2]][0], dp[1][dfs[0][2]][1])
    print(*ans[1:]) 
    return dp[1:].count(False), sum(ans[1:])

import random
from itertools import permutations
def generate_random_tree(n, weighted=False, weight_range=(1, 100)):
    nodes = list(range(1, n + 1))
    random.shuffle(nodes)
    edges = []
    in_tree = {nodes[0]}  # Start from a random node
    remaining = set(nodes[1:])
    while remaining:
        u = random.choice(list(in_tree))
        v = remaining.pop()
        w = random.randint(*weight_range) if weighted else None
        edges.append((u, v, w) if weighted else (u, v))
        in_tree.add(v)
    return edges

def brute(n, edges):
    if n == 2:
        print(2, 2)
        print(1, 1)
        exit(0)

    adj = [[] for _ in range(n)]
    for i in range(1, n):
        u, v = edges[i-1]
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    transition = [[] for _ in range(n)]
    dp = [
        [[0, 1] for _ in range(n)],
        [[1, len(adj[u])] for u in range(n)],
    ] # dp[maintain_sum][u] = [count, sum]

    ptr = 0
    stack = [(0, -1)]
    while ptr < len(stack):
        u, par = stack[ptr]
        ptr += 1
        for v in adj[u]:
            if v != par:
                stack.append((v, u))

    while len(stack) > 0:
        u, par = stack.pop()
        for v in adj[u]:
            if v != par:
                start = 0
                L, R = dp[0][v], dp[1][v]
                if L[0] < R[0] or L[0] == R[0] and L[1] > R[1]:
                    L = [R[0], R[1]]
                    start = 1
                
                dp[0][u][0] += L[0]
                dp[0][u][1] += L[1]
                transition[u].append((v, start))

                dp[1][u][0] += dp[0][v][0]
                dp[1][u][1] += dp[0][v][1]


    ans = [0] * n
    start = 0
    L, R = dp[0][0], dp[1][0]
    if L[0] < R[0] or L[0] == R[0] and L[1] > R[1]:
        L = R
        start = 1

    stack = [(0, -1, start)]
    while len(stack) > 0:
        u, par, state = stack.pop()
        ans[u] = 1 if state == 0 else len(adj[u])
        if state == 1:
            for v in adj[u]:
                if v != par:
                    stack.append((v, u, 0))
        else:
            for v, nstate in transition[u]:
                stack.append((v, u, nstate))

    print(L[0], L[1])
    print(' '.join(str(x) for x in ans))
    return L[0], L[1]
        
def checker():
    for i in range(10000):
        n = 20
        adj = [[] for i in range(n+1)]
        edges = generate_random_tree(n)
        for i in range(n-1):
            a, b = edges[i]
            adj[a].append(b)
            adj[b].append(a) 
        sol1, sol2 = solve(n, adj)
        brt1, brt2 = brute(n, edges)
        if sol1 != brt1 and sol2 != brt2:
            print(sol1, sol2, brt1, brt2)
            print("Found")
            print(adj)
            break
# checker()
n = int(input())
adj = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)  
solve(n, adj)

