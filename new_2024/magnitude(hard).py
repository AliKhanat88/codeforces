MOD = 998244353

def solve():
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    
    dp = [[0, 0] for i in range(n+1)]
    
    dp[0] = [(0, 1), None]
    for i in range(1, n + 1):
        # print(dp)
        maxi = abs(arr[i] + dp[i-1][0][0])
        if dp[i-1][1] != None:
            maxi = max(maxi, abs(arr[i] + dp[i-1][1][0]))
        count = 0
        if dp[i-1][0][0] + arr[i] == maxi:
            count += dp[i-1][0][1]
        if abs(dp[i-1][0][0] + arr[i]) == maxi:
            count += dp[i-1][0][1]
        if dp[i-1][1] != None:
            if abs(dp[i-1][1][0] + arr[i]) == maxi:
                count += dp[i-1][1][1]
            if dp[i-1][1][0] + arr[i] == maxi:
                count += dp[i-1][1][1]
        dp[i][0] = (maxi, count % MOD)
        mini = arr[i] + dp[i-1][0][0]
        if dp[i-1][1] != None:
            mini = min(mini, abs(arr[i] + dp[i-1][1][0]), arr[i] + dp[i-1][1][0])
        # print(mini, maxi)
        if mini == maxi:
            dp[i][1] = None
        else:
            count = 0
            if dp[i-1][0][0] + arr[i] == mini:
                count += dp[i-1][0][1]
            if abs(dp[i-1][0][0] + arr[i]) == mini:
                count += dp[i-1][0][1]
            if dp[i-1][1] != None:
                if abs(dp[i-1][1][0] + arr[i]) == mini:
                    count += dp[i-1][1][1]
                if dp[i-1][1][0] + arr[i] == mini:
                    count += dp[i-1][1][1]
            dp[i][1] = (mini, count % MOD)
    # print(dp)
    print(dp[-1][0][1])

for t in range(int(input())):
    solve()