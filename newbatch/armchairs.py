from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    loc = []
    for i in range(n):
        if arr[i] == 1:
            loc.append(i)

    if len(loc) == 0:
        print(0)
        return
    

    dp = [[None for i in range(n)] for i in range(len(loc))]
    
    for i in range(n):
        if arr[i] == 0:
            dp[0][i] = abs(loc[0] - i)


    for i in range(1, len(loc)):
        mini = None
        for j in range(n):
            if dp[i-1][j] != None:
                if mini == None:
                    dp[i][j] = None
                    mini = dp[i-1][j]
                else:
                    dp[i][j] = mini + abs(loc[i] - j)
                mini = min(mini, dp[i-1][j])
    mini = 9999999999999999999999
    # print(dp)
    for i in range(n):
        if dp[-1][i] != None:

            mini = min(mini, dp[-1][i])
    print(mini)




solve()