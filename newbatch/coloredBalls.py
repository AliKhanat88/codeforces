max = 5001
rem = 998244353

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    arr = [0] + arr

    dp = [[None for i in range(max)] for j in range(n+1)]
    for i in range(1, n+1):
        dp[i][arr[i]] = [0,1]

    ans = 0
    for i in range(2, n+1):
        for j in range(max): 
            if dp[i-1][j] != None:
                if j >= arr[i]:
                    add = arr[i]
                    temp = j - arr[i]
                else:
                    add = j
                    temp = arr[i] - j
                    if temp % 2 == 0:
                        add += temp // 2
                        temp = 0
                        
                    else:
                        add += (temp - 1) // 2
                        temp = 1

                if dp[i][temp] == None:
                    dp[i][temp] = [(dp[i-1][j][0] + dp[i-1][j][1] * add) % rem, dp[i-1][j][1] % rem]
                else:
                    dp[i][temp][0] = (dp[i][temp][0] + dp[i-1][j][0] + dp[i-1][j][1] * add) % rem
                    dp[i][temp][1] = (dp[i][temp][1] +  dp[i-1][j][1]) % rem
                if dp[i][j] == None:
                    dp[i][j] = dp[i-1][j][:]
                else:
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][0]) % rem
                    dp[i][j][1] = (dp[i][j][1] + dp[i-1][j][1]) % rem
            
    # print(dp) 
    ans = 0
    for i in range(max):
        if dp[-1][i] != None:
            ans += (dp[-1][i][0] + dp[-1][i][1] * i) % rem

    print(ans % rem)





solve()