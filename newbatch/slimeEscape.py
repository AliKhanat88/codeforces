def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    maxi_left = arr[k-1]
    maxi_right = arr[k-1]
    arr_sum = [0] * n
    if k-2 >= 0:
        arr_sum[k-2] = arr[k-2]
    if k < n:
        arr_sum[k] = arr[k]
    for i in range(k-3, -1, -1):
        arr_sum[i] = arr_sum[i+1] + arr[i]

    for i in range(k+1, n):
        arr_sum[i] = arr_sum[i-1] + arr[i]
    
    # print(arr_sum)

    p1 = k - 2
    p2 = k

    while True:
        old_p1, old_p2 = p1, p2
        while p1 >= 0 and maxi_right + arr_sum[p1] >= 0:
            maxi_left = max(maxi_left, arr_sum[p1] + arr[k-1])
            p1 -= 1
        
        while p2 < n and maxi_left + arr_sum[p2] >= 0:
            maxi_right = max(maxi_right, arr_sum[p2] + arr[k-1])
            p2 += 1
        # print(p1, p2,maxi_left, maxi_right)
        if p1 < 0 or p2 >= n:
            print("YES")
            return
        elif p1 == old_p1 and p2 == old_p2:
            print("NO")
            return
        
        


for t in range(int(input())):
    solve()