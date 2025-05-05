def get_temp(n, b, c):
    l = -1
    r = 10 ** 18
    while l + 1 < r:
        mid = (l + r) // 2
        if b*mid + c < n:
            l = mid
        else:
            r = mid - 1
    if b*r + c < n:
        return r
    return l

def solve():
    n, b, c = map(int, input().split())
    if b == 0:
        if c + 1 < n - 1:
            print(-1)
        elif c == n - 1:
            print(n-1)
        elif c == n - 2:
            print(n - 1)
        else:
            print(n)
        return

    print(n - get_temp(n, b, c) - 1)
for t in range(int(input())):
    solve()