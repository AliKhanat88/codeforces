from collections import defaultdict

def solve():
    # print("TEST")
    n = int(input())
    arr = list(map(int, input().split()))
    dict= defaultdict(lambda: - 1)
    per_arr = [0] * n
    for i, val in enumerate(arr):
        per_arr[i] = dict[val]
        dict[val] = i
    dp = [0] * n + [0]
    for i in range(n):
        if per_arr[i] == -1:
            dp[i+1] = dp[i]
        else:
            if i - per_arr[i] + dp[per_arr[i]] + 1 > dp[i]:
                dp[i] = i - per_arr[i] + dp[per_arr[i]]
                dp[i+1] = i - per_arr[i] + dp[per_arr[i]] + 1
            else:
                dp[i+1] = dp[i]
    # print(per_arr)
    print(dp[-1])
for t in range(int(input())):
    solve()