def solve():
    n = int(input())
    s = input()

    dp = [[0, 0] for i in range(n+4)]
    plus = n
    minus = 1
    ans = 0
    for i in range(n):
        dp[i][1] += plus
        dp[i][0] += 1
        if s[i] == "0":
            dp[i+1][0] += dp[i][0]
            dp[i+1][1] += (dp[i][1] - dp[i][0])
        else:
            ans += dp[i][1]
            dp[i+3][0] += dp[i][0]
            dp[i+3][1] += ((dp[i][1] - 3 * dp[i][0]))
        plus -= 1
        minus += 1
    # print(dp)
    print(ans)

for t in range(int(input())):
    solve()