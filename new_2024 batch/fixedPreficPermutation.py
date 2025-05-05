import sys
input = sys.stdin.readline
from bisect import bisect_right

def cus_sort(x):
    arr = [0] * len(x)
    for i in range(len(x)):
        arr[x[i] - 1] = i+1
    return tuple(arr)

# print(cus_sort((2, 3, 1, 4)))

def solve():
    n, m = map(int, input().split())
    arr = [0] * n
    for i in range(n):
        arr[i] = tuple(map(int, input().split()))

    sorted_arr = [0] * n
    for i in range(n):
        sorted_arr[i] = cus_sort(arr[i])
    sorted_arr = sorted(sorted_arr)
    # print("TEST")
    # print(sorted_arr)
    for i in range(n):
        index = bisect_right(sorted_arr, arr[i])
        index -= 1
        # print(arr[i], index)
        ans1 = 0
        for j in range(m):
            if arr[i][j] == sorted_arr[index][j]:
                ans1 += 1
            else:
                break
        if index + 1 < n:
            ans2 = 0
            for j in range(m):
                if arr[i][j] == sorted_arr[index+1][j]:
                    ans2 += 1
                else:
                    break
            print(max(ans1, ans2), end=" ")
        else:
            print(ans1, end =" ")
    print()
    

for t in range(int(input())):
    solve()