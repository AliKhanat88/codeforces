def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    dp = [0] * (n+1)

    for i in range(n):
        maxi = 1
        for j in range(i-1, max(-1, i - 500), -1):
            if (arr[j] ^ i) < (j ^ arr[i]):
                maxi = max(maxi, dp[j] + 1)
        dp[i] = maxi
    print(max(dp))

for t in range(int(input())):
    solve()