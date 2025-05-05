from bisect import bisect_right
from math import ceil

def checkComplete(x, arr):
    temp = bisect_right(arr, 2*x+arr[0])
    # print(temp)
    if temp >= len(arr):
        return 1
    else:
        temp = bisect_right(arr, 2*x+arr[temp])
        # print(temp)
        if temp >= len(arr):
            return 1
        else:
            temp = bisect_right(arr, 2*x+arr[temp])
            # print(temp)
            if temp >= len(arr):
                return 1
    return -1

def solve():
    n = int(input())
    arr = [*map(int, input().split())]

    arr.sort()

    # print(arr)
    # print(checkComplete(4, arr))

    low = 0
    high = 1000000000

    for i in range(100):
        mid = (high - low) // 2 + low
        temp = checkComplete(mid, arr)
        if temp == -1:
            low = mid +1
        else:
            high = mid
    print(low)
for t in range(int(input())):
    solve()