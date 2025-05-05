from collections import defaultdict


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    MOD = 998244353
    dict= defaultdict(lambda: 0)
    dp = [[0, 0] for i in range(n+1)]
    if arr[0] == 0:
        dp[1][0] = 1
        dp[1][1] = 1
        dict[0] += 1
        dict[1] += 1
    else:
        dp[1][1] = 1
        dict[1] += 1
    # print(arr)
    # print(dict)
    for i in range(1, n):
        dp_index = i + 1
        dp[dp_index][0] = dict[arr[i]]
        dp[dp_index][1] = dp[dp_index-1][0]
        # if dp[dp_index][0] == dp[dp_index][1] and dp[dp_index][0] == 0:
        #     print(0)
        #     return
        new_dict = defaultdict(lambda: 0)
        new_dict[arr[i]] = (new_dict[arr[i]] + dict[arr[i]]) % MOD
        new_dict[arr[i-1] + 1] = (new_dict[arr[i-1] + 1] + dp[dp_index-1][0]) % MOD
        dict = new_dict
        # print(dict)
    # print(dp)
    print((dp[n][0] + dp[n][1]) % MOD)
        



for t in range(int(input())):
    solve()