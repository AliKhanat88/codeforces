def check(arr, rem, k, x):
    dp = [0] * rem
    i = 0
    while i < len(arr):
        if arr[i] >= x:
            dp[i % k] = max(dp[i % k], 1)
        j = i + 1
        while j < i + rem:
            if arr[j] >= x:
                dp[j % k] = max(dp[j % k], dp[j % k - 1] + 1)
            else:
                dp[j % k] = max(dp[j % k], dp[j % k - 1])
            j += 1
        i += k
    # print(dp)
    if dp[-1] >= (rem + 2) // 2:
        return True
    return False

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if n % k == 0:
        rem = k
    else:
        rem = n % k

    # print(check(arr, rem, k, 6))
    # return
    l = 1
    r = 10 ** 9
    while l + 1 < r:
        m = (l + r) // 2
        temp = check(arr, rem, k, m)
        if temp:
            l = m 
        else:
            r = m - 1
    if check(arr,rem, k, r):
        print(r)
    else:
        print(l)
    
    

for t in range(int(input())):
    solve()