def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    maxi = -1
    maxi_index = -1
    for i, num in enumerate(arr):
        if num > maxi:
            maxi = num
            maxi_index = i

    maxi1 = -1
    maxi2 = -1
    maxi3 = maxi

    for i in range(n):
        maxi1 = max(maxi1, arr[i]+i)
        maxi2 = max(maxi2, arr[i] + n - i - 1) 
        if i == maxi_index:
            continue
        elif i > maxi_index:
            maxi3 = max(maxi3, arr[i] + i)
        else:
            maxi3 = max(maxi3, arr[i] + n - i - 1)
    print(min(maxi1, maxi2, maxi3))

# for t in range(int(input())):
solve()