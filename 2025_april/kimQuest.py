MOD = 998244353
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    per_even = 0
    per_odd = 0
    dp = [[0, 0, 0] for i in range(n+1)]
    ans = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            dp[i+1][0] += per_odd
            ans -= per_odd
            dp[i+1][0] += dp[i][2]
            per_even += 1
            
        else:
            dp[i+1][1] += per_even
            dp[i+1][2] += per_odd
            ans -= per_even
            ans -= per_odd
            dp[i+1][1] += dp[i][0]
            dp[i+1][2] += dp[i][1]
            per_odd += 1
        for j in range(3):
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD

    # print(dp)
    ans = dp[-1][0] + dp[-1][1] + dp[-1][2] + ans + (1 << per_even) - per_even - ((per_even) * (per_even - 1)) // 2 - 1
    print(ans % MOD)




solve()