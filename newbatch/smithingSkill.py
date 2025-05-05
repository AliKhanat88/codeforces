import sys
input = sys.stdin.readline
from collections import defaultdict


MAX = 1000001
def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    crr = list(map(int, input().split()))

    dict = defaultdict(lambda:-1)
    for i in range(n):
        dict[arr[i]] = max(dict[arr[i]], brr[i])

    dp = [0] * MAX
    min_diff_ind = (MAX, 0)
    for i in range(1, MAX):
        if dict[i] == -1 and min_diff_ind == (MAX, 0):
            continue
        if dict[i] != -1:
            if i - dict[i] < min_diff_ind[0] - min_diff_ind[1]:
                min_diff_ind = (i, dict[i])

        # print(min_diff_ind)
        dp[i] = dp[i-min_diff_ind[0] + min_diff_ind[1]] + 2
    ans = 0
    for i in range(m):
        if crr[i] >= MAX:
            if (crr[i] - min_diff_ind[0]) % (min_diff_ind[0] - min_diff_ind[1]) == 0:
                div = (crr[i] - min_diff_ind[0]) // (min_diff_ind[0] - min_diff_ind[1])
            else:
                div = (crr[i] - min_diff_ind[0]) // (min_diff_ind[0] - min_diff_ind[1]) + 1
            ans += (div * 2)
            crr[i] = crr[i] - div * (min_diff_ind[0] - min_diff_ind[1])
        # print(crr[i])
        if crr[i] < 0:
            ans -= 2
        ans += dp[crr[i]]
    # print(dp)
    print(ans)




    

solve()