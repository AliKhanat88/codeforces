def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    adj = [[] for i in range(n+1)]
    for i in range(2, n+1):
        adj[arr[i-2]].append(i)
    # print(adj)
    dfs = [1]
    for cur in dfs:
        for child in adj[cur]:
            dfs.append(child)
    
    dp = [[] for i in range(n+1)]
    arr = [-1, 0] + arr 
    for v in dfs[::-1]:
        p = arr[v]
        if len(dp[v]) == 0:
            dp[p].append([1, 0])
        else:
            maxi = max(dp[v])
            dp[v].remove(maxi)
            sumi = 0
            for num in dp[v]:
                sumi += (num[0] + num[1] * 2)
            dp[v].append(maxi)
            if maxi[0] > sumi:
                dp[p].append([maxi[0] - sumi + 1, sumi + maxi[1]])
            else:
                dp[p].append([(sumi + maxi[0]) % 2 + 1, maxi[1] + (sumi + maxi[0]) // 2])
    # print(dp)
    print(dp[0][0][1])

        


for t in range(int(input())):
    solve()