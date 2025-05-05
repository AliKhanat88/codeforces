# import time

# start_time = time.time()
M = 10 ** 9 + 7
mult_104 = pow(10000, M-2, M)
MAX = 1025
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    prr = list(map(int, input().split()))
    if n == 1:
        print(arr[0])
        return
    dp = [[0, 0] for i in range(MAX)]
    dp[0][0] = 1
    temp = 1
    # print(mult_104)
    reverse_power = [[0 for i in range(2)] for i in range(n)]
    for i in range(n):
        reverse_power[i][0] = (1 - (prr[i] * mult_104) % M) % M
        reverse_power[i][1] = (pow(reverse_power[i][0], M-2, M) * prr[i] * mult_104) % M
    for i in range(n):
        temp = (temp * reverse_power[i][0]) % M
    dp[0][1] = temp
    # print(dp)
    
    for i in range(1, n+1):
        # print(i)
        new_dp = [[0, 0] for i in range(MAX)]
        for j in range(MAX-1):
            new_dp[j][0] = (new_dp[j][0] + dp[j][0]) % M
            new_dp[j][1] = (new_dp[j][1] + dp[j][1]) % M
            if dp[j] != 0:

                new_dp[j^arr[i-1]][0] = (new_dp[j^arr[i-1]][0] + dp[j][0]) % M
                new_dp[j^arr[i-1]][1] = (new_dp[j^arr[i-1]][1] + dp[j][1] * reverse_power[i-1][1]) % M
        dp = new_dp
    # print(dp)
    ans = 0
    for i in range(MAX):
        ans += (i ** 2 * new_dp[i][1]) % M
    print(ans % M)
for t in range(int(input())):
    solve()


# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")