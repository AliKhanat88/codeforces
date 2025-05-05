def solve():
    n, m = map(int, input().split())

    arr = [0] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    dp = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(1, n + 1):
        for j in range(1, m+ 1):
            dp[i][j] = max(dp[i-1][j] + arr[i-1][j-1], dp[i][j-1] + arr[i-1][j-1])
    print(dp[n][m])
for t in range(int(input())):
    solve()