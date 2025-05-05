from collections import defaultdict

def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    maxi = -1
    for i in range(1, n-1):
        if arr[i] <= arr[i+1]:
            maxi = max(maxi, arr[i])
        if arr[i] <= arr[i-1]:
            maxi = max(maxi, arr[i])

    if arr[0] <= arr[1]:
        maxi = max(maxi, arr[0])
    if arr[-1] <= arr[-2]:
        maxi = max(maxi, arr[-1])

    for i in range(2, n):
        if arr[i-1] >= arr[i] or arr[i-2] >= arr[i]:
            maxi = max(maxi, arr[i])
        if arr[i] >= arr[i-1] or arr[i-2] >= arr[i-1]:
            maxi = max(maxi, arr[i-1])
        if arr[i] >= arr[i-2] or arr[i-1] >= arr[i-2]:
            maxi = max(maxi, arr[i-2])
    
    print(maxi)


for t in range(int(input())):
    solve()