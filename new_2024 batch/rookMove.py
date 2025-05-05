import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())

    for i in range(k):
        a, b = map(int, input().split())
        if a != b:
            n -= 2
        else:
            n -= 1
    dp = [1] * (n+1)
    for i in range(2, n+1):
        dp[i] = ((i + i - 2) * (dp[i-2]) + dp[i-1]) % (10 ** 9+7)
    print(dp[-1])

for i in range(int(input())):
    solve()