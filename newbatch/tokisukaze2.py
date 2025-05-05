def solve(n, s):
    
    dp = [[0,0] for i in range(n)]
    oper =0
    if s[0] == "0" and s[1] == "0":
        dp[1][0] = 1
        dp[1][1] = float("inf")
    elif s[0] == "1" and s[1] == "1":
        dp[1][1] = 1
        dp[1][0] = float("inf")
    else:
        dp[1][0] = 1
        dp[1][1] = 1
        oper += 1
    
    for i in range(3, n, 2):
        if s[i] != s[i-1]:
            oper += 1
            dp[i][0] = min(dp[i-2][0], dp[i-2][1] + 1)
            dp[i][1] = min(dp[i-2][0] + 1, dp[i-2][1])
        elif s[i] == "0":
            dp[i][0] = min(dp[i-2][0], dp[i-2][1] + 1)
            dp[i][1] = float("inf")
        elif s[i] == "1":
            dp[i][0] = float("inf")
            dp[i][1] = min(dp[i-2][0] + 1, dp[i-2][1])
    print(oper, min(dp[-1][0], dp[-1][1]))
    return min(dp[-1][0], dp[-1][1])


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        s = input()
        solve(n, s)