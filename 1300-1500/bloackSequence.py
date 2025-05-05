def solve():
    n = int(input())
    arr = [*map(int, input().split())]

    dp = [99999999] * (n+1)
    min_length = 0
    dp[0] = 0
    for i in range(n):
        dp[i] = min(dp[i], dp[min_length] + i - min_length)
        # print(dp)
        if i + arr[i] + 1 <= n:
            dp[i + arr[i] + 1] = min(dp[i], dp[i + arr[i] + 1])
        if n - min_length + dp[min_length] > n - i + dp[i]:
            min_length = i
        # print(dp)
    mini = dp[-1]
    for i in range(n):
        mini = min(mini, dp[i] + n - i)
    print(mini)
    # print(dp)

for t in range(int(input())):
    solve()