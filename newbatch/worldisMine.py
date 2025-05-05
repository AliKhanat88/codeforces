from collections import Counter
import sys
input = sys.stdin.readline

inf = 999999999999999
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    d_arr = []
    c = Counter(arr)
    for key in sorted(c):
        d_arr.append([key, c[key]])

    # print(d_arr)
    if len(d_arr) == 1:
        print(1)
        return

    dp = [[float("inf") for i in range(len(d_arr) + 1)] for i in range(len(d_arr))]

    dp[0][1] = 1
    for i in range(1, len(d_arr)):
        for j in range(len(d_arr)):
            if j >= d_arr[i][1]:
                dp[i][j-d_arr[i][1]] = min(dp[i][j-d_arr[i][1]], dp[i-1][j])
            dp[i][j+1] = min(dp[i][j+1], dp[i-1][j] + 1)
    print(min(dp[-1]))
        
for t in range(int(input())):
    solve()