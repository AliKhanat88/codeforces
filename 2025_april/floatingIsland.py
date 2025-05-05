MOD = 10 ** 9 + 7
def factorial(x):
    res = 1
    for i in range(2, x+1):
        res = (res * i) % MOD

    return res % MOD

def inv(x):
    return pow(x, MOD - 2, MOD)

def solve():
    n, k = map(int, input().split())
    adj = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    if k == 1 or k == 3:
        print(1)
        return
    
    dfs = [(1, -1)]
    for v, p in dfs:
        for child in adj[v]:
            if child != p:
                dfs.append((child, v))

    ans = 0
    dp = [0] * (n+1)
    count = [0] * (n+1)
    for v, p in dfs[::-1]:
        
        sumi = 0
        for child in adj[v]:
            if child != p:
                sumi += count[child]
                count[v] += count[child]
                dp[v] += dp[child]
        
        dp[v] += count[v]
        if count[v] == 0:
            dp[v] = 0
        ans += dp[v]
        count[v] += 1
        for child in adj[v]:
            if child != p:
                ans += ((sumi - count[child]) * (dp[child] + count[child]))
    # print(ans)
    # print(dp)
    # print(count)
    temp = (n * (n-1)) // 2
    ans = (ans + temp)
    # print(ans, "After adding")
    print((ans * inv(temp)) % MOD)

solve()