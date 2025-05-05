def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n == 1:
        print(arr[0])
        return
    # print("TEST")
    # print(arr)
    dp = [[0 for i in range(n+1)] for i in range(k+1)]    
    for i in range(1, n):
        for j in range(i - 1, max(-1, i - k -1), -1):
            sumi = sum(arr[j:i+1]) - (min(arr[j:i+1]) * (i-j+1))
            size = i - j
            for l in range(k):
                if l + size <= k and l + size >= 0 >= 0:
                    dp[l + size][i] = max(dp[l + size][i], dp[l][i-size-1] + sumi)
        for j in range(k+1):
            dp[j][i] = max(dp[j][i], dp[j][i-1])
        # print("i dp", dp, i)
    print(sum(arr) - max(dp[k]))


for t in range(int(input())):
    solve()