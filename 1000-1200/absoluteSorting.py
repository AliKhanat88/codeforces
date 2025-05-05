from math import ceil, floor
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    lower = 0
    upper = 99999999999999999999999999999999999999999
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            continue
        temp = (arr[i] + arr[i-1]) / 2
        if arr[i] > arr[i-1]:
            temp = floor(temp)
            upper = min(upper, temp)
        elif arr[i] < arr[i-1]:
            temp = ceil(temp)
            lower = max(temp, lower)
    if lower > upper:
        print(-1)
        return
    else:
        print(lower)

for t in range(int(input())):
    solve()