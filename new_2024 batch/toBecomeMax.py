def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # print("TEST")
    # print(n, k)
    # print(arr)
    
    i = n - 1
    last = n-1
    while i > -1:
        if arr[i] > arr[last] + (last - i):
            last = i
        i -= 1
    last += 1
    # print(last)
    dp = [999999999999999 for i in range(last)]

    for i in range(last):
        goal = arr[last-1] -i
        sumi = 0
        for j in range(last-1, -1, -1):
            if arr[j] >= goal:
                sumi = 0
            else:
                sumi = sumi + goal - arr[j]
            if goal >= arr[last-1]:
                dp[goal - arr[last-1]] = min(sumi, dp[goal - arr[last-1]])
            # print(dp, goal)
            goal += 1
    
    for i in range(len(dp)-1, -1, -1):
        if dp[i] <= k:
            print(arr[last-1] + i)
            break
    # print(dp)

    
for t in range(int(input())):
    solve()