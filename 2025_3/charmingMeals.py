def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    arr.sort()
    brr.sort()
    # print(arr)
    # print(brr)
    maxi = -1
    for i in range(n+1):
        temp_mini = 1 << 64
        # print(i)
        for j in range(i):
            temp_mini = min(temp_mini, brr[n-i+j] - arr[j])
        for j in range(n-i):
            temp_mini = min(temp_mini, arr[i+j] - brr[j])
        maxi = max(maxi, temp_mini)
    print(maxi)




for t in range(int(input())):
    solve()