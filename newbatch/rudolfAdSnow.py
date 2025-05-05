from math import log2, ceil
def checker(i, x):
    mult = x + 1
    for i in range(i):
        mult = mult * x + 1
    return mult

def solve():
    n = int(input())
    for i in range(1, 60):
        lower = 2
        higher = ceil(n ** (1 / (i+1)))
        while lower + 1 < higher:
            mid = lower + (higher - lower) // 2
            temp = checker(i, mid)
            if temp == n:
                lower = mid
                higher = mid
                break
            elif temp < n:
                lower = mid + 1
            elif temp > n:
                higher = mid - 1

        if checker(i, lower) == n:
            print("YES")
            return
        if checker(i, higher) == n:
            print("YES")
            return
    print("NO")

for t in range(int(input())):
    solve()