from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c = Counter(arr)
    # print("TEST")
    for i in range(0, n+2):
        if c[i] == 0:
            mex = i
            break

    inf = 9999999999999
    dp = [inf] * (mex+1)

    # print([c[i] for i in range(mex+1)])
    dp[-1] = 0
    # print(dp)
    for i in range(mex-1, -1, -1):
        for j in range(i+1,mex+1):
            dp[i] = min((c[i] - 1) * j + dp[j] + i, dp[i])
        # print(dp)

    print(dp[0])





for t in range(int(input())):
    solve()