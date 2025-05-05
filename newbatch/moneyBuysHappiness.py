import sys
input = sys.stdin.readline

inf = 9999999999999999

def solve():
    m, x = map(int, input().split())

    cost = [0] * m
    happy = [0] * m
    for i in range(m):
        cost[i], happy[i] = map(int, input().split())

    # print(cost)
    # print(happy)
    total = sum(happy)
    dp = [[inf for i in range(total + 1)] for j in range(m+1)]

    dp[0][0] = 0
    for i in range(1, m+1):
        for j in range(total+1):
            if j >= happy[i-1] and dp[i-1][j - happy[i-1]] + cost[i-1] <= (i-1) * x:
                dp[i][j] = min(dp[i][j], dp[i-1][j], dp[i-1][j - happy[i-1]] + cost[i-1])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
    # print(dp[1:])
    for i in range(len(dp[-1])-1, -1, -1):
        if dp[-1][i] <= (m-1) * x:
            print(i)
            return


for t in range(int(input())):
    solve()