import sys
input = sys.stdin.readline
from math import gcd, isqrt

def solve():
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    dp = [[0 for i in range(m)] for i in range(n)]
    d = 1
    temp = isqrt(arr[0][0])
    ans = 1
    while d <= temp:
        if arr[0][0] % d == 0:
            dp[0][0] = 1
            for i in range(1, m):
                if dp[0][i-1] == 1 and arr[0][i] % d == 0:
                    dp[0][i] = 1
                else:
                    dp[0][i] = 0
            for i in range(1, n):
                if dp[i-1][0] == 1 and arr[i][0] % d == 0:
                    dp[i][0] = 1
                else:
                    dp[i][0] = 0
            
            for i in range(1, n):
                for j in range(1, m):
                    if (dp[i-1][j] == 1 or dp[i][j-1] == 1) and arr[i][j] % d == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
            if dp[-1][-1] == 1:
                ans = max(ans, d)

            dp[0][0] = 1
            for i in range(1, m):
                if dp[0][i-1] == 1 and arr[0][i] % (arr[0][0] // d) == 0:
                    dp[0][i] = 1
                else:
                    dp[0][i] = 0
            for i in range(1, n):
                if dp[i-1][0] == 1 and arr[i][0] % (arr[0][0] // d) == 0:
                    dp[i][0] = 1
                else:
                    dp[i][0] = 0
            
            for i in range(1, n):
                for j in range(1, m):
                    if (dp[i-1][j] == 1 or dp[i][j-1] == 1) and arr[i][j] % (arr[0][0] // d) == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
            if dp[-1][-1] == 1:
                ans = max(ans, (arr[0][0] // d))
        d += 1
    
    print(ans)

for t in range(int(input())):
    solve()