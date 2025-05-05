for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = -1
    for i in range(0, n, 2):
        maxi = max(maxi, arr[i])
    print(maxi)