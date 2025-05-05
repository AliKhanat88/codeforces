from heapq import heapify, heappop

def solve():
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    for i in range(n, 0, -1):
        j = 2
        while i * j <= n:
            arr[i] = max(arr[i], arr[i*j])
            j += 1
    
    # print(arr)
    heapify(arr)

    heappop(arr)
    ans = 0
    temp = 1
    while arr:
        ans = (ans + heappop(arr) * temp) % 998244353
        temp = (temp * 2) % 998244353
    print(ans)



solve()