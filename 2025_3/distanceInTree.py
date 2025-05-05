def solve():
    n, k = map(int, input().split())
    adj = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    # print(adj)
    dfs = [(1, -1)]
    for v, p in dfs:
        for child in adj[v]:
            if child != p:
                dfs.append((child, v))
    
    dp = [0] * (n+1)
    ans = 0
    for v, p in dfs[::-1]:
        if p in adj[v]:
            adj[v].remove(p)
        if len(adj[v]) == 0:
            temp = [0] * (k+1)
            temp[1] = 1
            dp[v] = temp
            continue
        suffix = [[0 for i in range(k+1)] for i in range(len(adj[v]))]

        for i in range(len(adj[v])-1, -1, -1):
            for j in range(1, k+1):
                if i+1 >= len(adj[v]):
                    suffix[i][j] = dp[adj[v][i]][j]
                    continue
                suffix[i][j] = suffix[i+1][j] + dp[adj[v][i]][j]
        # print("vertex in dp", v)
        # print(suffix)

        for i in range(len(adj[v])-1):
            for j in range(1, k):
                ans += (dp[adj[v][i]][j] * suffix[i+1][k-j])
        dp[v] = suffix[0]
        ans += dp[v][k]
        for i in range(k-1, 0, -1):
            dp[v][i+1] = dp[v][i]
        dp[v][1] = 1
    # print(dp)
    print(ans)




solve()