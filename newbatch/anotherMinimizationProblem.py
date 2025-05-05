

inf = float("inf")
max_weight = 10001

def solve():
    n = int(input())
    arr = list(reversed(list(map(int, input().split()))))
    brr = list(reversed(list(map(int, input().split()))))

    prefix = [0] * (n+1)

    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + arr[i-1] + brr[i-1]

    # print(prefix)

    dp = [[inf for i in range(max_weight)] for i in range(n)]

    for i in range(max_weight):
        if i == arr[0] or i == brr[0]:
            dp[0][i] = 0

    for i in range(1, n):
        for j in range(max_weight):
            if j > arr[i]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-arr[i]] + (j-arr[i]) * arr[i] + (prefix[i] - (j - arr[i])) * brr[i])
            if j > brr[i]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-brr[i]] + (j-brr[i]) * brr[i] + (prefix[i] - (j - brr[i])) * arr[i])
    # print("TEST")
    # print(arr)
    # print(brr)
    # print(dp)
    # print(min(dp[-1]))
    ans = min(dp[-1]) * 2
    for i in range(n):
        ans += ((n-1) * arr[i] ** 2)
        ans += ((n-1) * brr[i] ** 2)
    print(ans)


for t in range(int(input())):
    solve()