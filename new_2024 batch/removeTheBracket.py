def solve():
    n, s = map(int, input().split())

    arr = list(map(int, input().split()))

    # print("TEST")
    # print(arr, s)

    arr_pair = [0] * n
    for i in range(1, n-1):
        if arr[i] > s:
            temp1 = s
            temp2 = arr[i] - s
            arr_pair[i] = (min(temp1, temp2), max(temp1, temp2))
        else:
            arr_pair[i] = (0, arr[i])

    arr_pair[-1] = (arr[-1], arr[-1])
    arr_pair[0] = (arr[0], arr[0])
    # print(arr_pair)
    dp = [[0 for i in range(2)] for i in range(n)]

    
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0] + arr_pair[i][0] * arr_pair[i-1][1], dp[i-1][1] + arr_pair[i][0] * arr_pair[i-1][0])
        dp[i][1] = min(dp[i-1][0] + arr_pair[i][1] * arr_pair[i-1][1], dp[i-1][1] + arr_pair[i][1] * arr_pair[i-1][0])
    
    # print(dp)
    # print(min(dp[-1][0], dp[-1][1]))
    print(min(dp[-1][0], dp[-1][1]))

if __name__ == "__main__":
    for t in range(int(input())):
        solve()