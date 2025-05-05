inf = 99999999999999999999
def solve():
    n, k = map(int, input().split())
    temp_k = k
    k = k + 5
    mini_arr = [inf] * (k + 1)
    mini_arr[0] = 0
    for i in range(n):
        a, b = map(int, input().split())
        dp = []
        dp.append(mini_arr)
        while True:
            # print(a, b)
            if a == 1 and b == 1:
                new_arr = [inf] * (k+1)
                for j in range(k-1):
                    new_arr[j+2] = min(new_arr[j+2], dp[-1][j] + 1)
                dp.append(new_arr)
                break
            else:
                new_arr = [inf] * (k+1)
                if a >= b:
                    temp = b
                    a -= 1
                else:
                    temp = a
                    b -= 1
                for j in range(k):
                    new_arr[j+1] = min(new_arr[j+1], dp[-1][j] + temp)
                dp.append(new_arr)
        # print(dp)
        for j in range(len(dp)):
            for l in range(len(dp[j])):
                mini_arr[l] = min(mini_arr[l], dp[j][l])
    mini = inf
    for j in range(temp_k, k+1):
        mini = min(mini, mini_arr[j])
    if mini < inf:
        print(mini)
    else:
        print(-1)



for t in range(int(input())):
    solve()