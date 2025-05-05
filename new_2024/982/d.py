import sys
input = sys.stdin.readline
from bisect import bisect_left

inf = 99999999999999999999999
def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    # if max(arr) > brr[0]:
    #     print(-1)
    #     return
    sumi_arr = [0] * (n + 1)
    for i in range(1, n + 1):
        sumi_arr[i] = sumi_arr[i-1] + arr[i-1]
    mini_dp = [inf] * (n+1)
    # print(sumi_arr)
    # print(mini_dp)
    mini_dp[0] = 0
    # brr.sort()
    maxi_arr = [0] * n
    maxi = -1
    for i in range(n-1, -1, -1):
        maxi = max(maxi, arr[i])
        maxi_arr[i] = maxi
    
    # print(maxi_arr)

    for i in range(m):
        j = 1
        while j < n + 1:
            if maxi_arr[j-1] > brr[i]:
                j += 1
                continue
            temp_index = bisect_left(sumi_arr, sumi_arr[j] - brr[i])
            # print(j, temp_index, brr[i])
            mini_dp[j] = min(mini_dp[j], mini_dp[temp_index] + m - (i + 1))
            j += 1
            
    if mini_dp[-1] >= inf:
        print(-1)
    else:
        print(mini_dp[-1])
        

for t in range(int(input())):
    solve()