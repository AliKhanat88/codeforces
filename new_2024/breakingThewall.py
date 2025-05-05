# from collections import heapify, heappop, heappush

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    mini = float("inf")
    for i in range(1, n-1):
        if arr[i-1] % 2 == 0 and arr[i+1] % 2 == 0:
            mini = min(mini, arr[i-1] // 2 + arr[i+1] // 2)
        else:
            mini = min(mini, arr[i-1] // 2 + arr[i+1] // 2 + 1)
    for i in range(1,n):
        temp_maxi = max(arr[i], arr[i-1])
        temp_mini = min(arr[i], arr[i-1])
        if temp_maxi // 2 > temp_mini:
            mini = min(mini, temp_maxi // 2 + temp_maxi % 2)
        else:
            if (temp_maxi + temp_mini) % 3 == 0:
                mini = min(mini, (temp_maxi + temp_mini) // 3)
            else:
                mini = min(mini, (temp_maxi + temp_mini) // 3 + 1)
    mini1 = min(arr)
    arr.remove(mini1)
    mini2 = min(arr)
    mini = min(mini, (mini1 // 2 + mini1 % 2 + mini2 // 2 + mini2 % 2))

    print(mini)

solve()