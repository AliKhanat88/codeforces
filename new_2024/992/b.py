import sys
input = sys.stdin.readline

N = 10 ** 5 + 1
dp = [-1] * N
dp[1] = 1
for i in range(2, N):
    if dp[i] == -1:
        for j in range(i, min(N, 2 * i + 1)):
            dp[j] = dp[i-1] + 1



def solve():
    n = int(input())
    print(dp[n])

    
for t in range(int(input())):
    solve()