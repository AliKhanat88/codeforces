from collections import defaultdict

def solve():
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    adj = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    dfs = [(1, 0)]
    for v, p in dfs:
        for child in adj[v]:
            if p != child:
                dfs.append((child, v))

    # print(dfs)
    dp = [None] * (n+1)
    ans = 0
    for v, p in dfs[::-1]:
        maxi = -1
        max_dict = None
        for child in adj[v]:
            if child != p and len(dp[child]) > maxi:
                maxi = len(dp[child])
                max_dict = child
            
        if maxi == -1:
            dp[v] = defaultdict(lambda: 0)
            dp[v][arr[v]] += 1
        else:
            maxi_dict = dp[max_dict]
            
            dp[max_dict] = None
            # print(maxi_dict)
            ans += maxi_dict[arr[v]]
            for child in adj[v]:
                if child != p and dp[child] != None:
                    for key, val in dp[child].items():
                        if key == arr[v]:
                            ans += val
                        else:
                            ans += maxi_dict[key] * val
                            maxi_dict[key] += val
            maxi_dict[arr[v]] = 1
            dp[v] = maxi_dict
        # print(ans, v, p)
        # print(dp)

    print(ans)




for t in range(int(input())):
    solve()