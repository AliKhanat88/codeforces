import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    arr = sys.stdin.read().split()
    arr.sort()
    # print(arr)
    ans = 0
    for i in range(n):
        ans += (len(arr[i]) * n) * 2
        l = 0
        r = n - 1
        for j in range(len(arr[i])):
            matc = arr[i][-1-j]
            lower = l
            upper = r
            while lower + 1 < upper:
                mid = lower + (upper - lower) // 2
                if len(arr[mid]) <= j or arr[mid][j] < matc:
                    lower = mid + 1
                elif arr[mid][j] >= matc:
                    upper = mid
            if len(arr[lower]) > j and arr[lower][j] == matc:
                l = lower
            elif len(arr[upper]) > j and arr[upper][j] == matc:
                l = upper
            else:
                break
            lower = l
            upper = r
            while lower + 1 < upper:
                mid = lower + (upper - lower) // 2
                if arr[mid][j] == matc:
                    lower = mid
                elif arr[mid][j] > matc:
                    upper = mid - 1
            if arr[upper][j] == matc:
                r = upper
            elif arr[lower][j] == matc:
                r = lower
            else:
                break
            ans = ans - (r - l + 1) * 2
    print(ans)
                

        


solve()