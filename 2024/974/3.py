from decimal import Decimal
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1 or n == 2:
        print(-1)
        return
    sumi = sum(arr)
    arr.sort()
    temp = arr[n // 2]
    l = 0
    r = 10 ** 12
    while l + 1 < r:
        m = (l + r) // 2
        if Decimal((sumi + m)) / Decimal((2 * n)) > temp:
            r = m
        else:
            l = m + 1
    if Decimal((sumi + l)) / Decimal((2 * n)) > temp:
        print(l)
    else:
        print(r)
for t in range(int(input())):
    solve()