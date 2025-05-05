from bisect import bisect_left, bisect_right
def solve():
    n, c = map(int, input().split())

    arr = list(set(map(int, input().split())))
    arr.sort()

    j = 0
    for i in range(1, c+1):
        if j >= len(arr):
            break
        if arr[j] > i:
            temp = bisect_right(arr, c // i)
            for k in range(temp):
                templ = bisect_left(arr, arr[k] * i)
                tempr = bisect_right(arr, (i + 1) * arr[k] - 1)
                if tempr - templ >= 1:
                    print("No")
                    return
        else:
            j += 1
    print("Yes")
for t in range(int(input())):
    solve()