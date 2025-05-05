def solve():
    n = int(input())
    parent = list(map(int, input().split()))
    
    adj = [[] for i in range(n+1)]
    for i in range(n-1):
        # print(i, n)
        adj[parent[i]].append(i + 2)
    dfs = [(1, 0)]
    for v, p in dfs:
        for child in adj[v]:
            dfs.append((child, v))
    
    dp = [[] for i in range(n+1)]
    for v, p in dfs[::-1]:
        
        if len(adj[v]) == 0:
            dp[p].append(0)
        elif len(adj[v]) == 1:
            dp[p].append(dp[v][0] + 1)
        else:
            dp[v].sort(reverse=True)
            ans = [dp[v][0]]
            for i in range(1, len(dp[v])):
                num = dp[v][i]
                while len(ans) > 0 and ans[-1] == num:
                    num += 1
                    ans.pop()
                ans.append(num)
            if len(ans) == 1:
                dp[p].append(ans[0])
            else:
                dp[p].append(ans[0] + 1)
    # print(dp)
    print(dp[0][0])



for t in range(int(input())):
    solve()