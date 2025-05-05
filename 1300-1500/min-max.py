def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    maxi_arr = [0] * n
    mini_arr = [0] * n
    last = n-1
    for i in range(n-1, 0, -1):
        maxi_arr[i] = str(b[last] - a[i])
        if a[i] - b[i-1] > 0:
            last = i - 1
    maxi_arr[0] = str(b[last] - a[0])
    last = 0
    j = 0
    for i in range(n):
        while j < n - 1:
            if a[i] <= b[j]:
                break
            j += 1
        mini_arr[i] = str(b[j] - a[i])

    print(" ".join(mini_arr))
    print(" ".join(maxi_arr))



for t in range(int(input())):
    solve()
