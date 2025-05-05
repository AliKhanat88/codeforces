def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(1, n, 2):
        if arr[i-1] - arr[i] <= k:
            k -= (arr[i-1] - arr[i])
            arr[i] = arr[i-1]
        else:
            arr[i] += k
            k = 0
    # print(arr)
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += arr[i]  
        else:
            ans -= arr[i]  
    print(ans)     



for t in range(int(input())):
    solve()