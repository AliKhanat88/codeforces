import sys
input = sys.stdin.readline

inf = 10 ** 23
def solve():
    n, m = map(int, input().split())
    initial = int(input().strip(), 2)
    arr = [0] * (m)
    for i in range(m):
        cost = int(input())
        andi = int(input().strip(), 2)
        ori = int(input().strip(), 2)
        arr[i] = [cost, andi, ori]
    
    # print(arr)
    bits = 2048
    dp = [inf] * bits
    
    dp[initial] = 0
    for i in range(m):
        new_dp = [inf] * bits
        index = i % m
        for k in range(bits):
            if dp[k] < inf:
                new_dp[k] = min(new_dp[k], dp[k])
                new_dp[((k & arr[index][1]) ^ k) | arr[index][2]] = min(new_dp[((k & arr[index][1]) ^ k) | arr[index][2]], dp[k] + arr[index][0])
        dp = new_dp
    # print(dp[-1][5])
    if dp[0] == inf:
        print(-1)
    else:
        print(dp[0])


for t in range(int(input())):
    solve()