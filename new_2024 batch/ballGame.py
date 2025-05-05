import sys
input = sys.stdin.readline

def solve():
    n, m, x = map(int, input().split())

    dp = [[False for i in range(n+1)] for i in range(m+1)]
    dp[0][x] = True

    for i in range(1, m+1):
        temp = input().split()
        for j in range(1, n+1):
            if dp[i-1][j] == True:
                if temp[1] == "0":
                    if j+int(temp[0]) > n:
                        dp[i][(j+int(temp[0])) - n] = True
                    else:
                        dp[i][(j+int(temp[0]))] = True
                elif temp[1] == "1":
                    if j - int(temp[0]) < 1:
                        dp[i][n + j - int(temp[0])] = True
                    else:
                        dp[i][j - int(temp[0])] = True
                else:
                    if j - int(temp[0]) < 1:
                        dp[i][n + j - int(temp[0])] = True
                    else:
                        dp[i][j - int(temp[0])] = True
                    if j+int(temp[0]) > n:
                        dp[i][(j+int(temp[0])) - n] = True
                    else:
                        dp[i][(j+int(temp[0]))] = True
    ans = []
    for i in range(1, n+1):
        if dp[m][i] == True:
            ans.append(str(i))
    print(len(ans))
    print(" ".join(ans))
for t in range(int(input())):
    solve()