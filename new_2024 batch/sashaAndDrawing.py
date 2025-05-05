def solve():
    n, k = map(int, input().split())

    if k == 4 * n - 2:
        print(n+n)
    elif k == 4 * n - 3:
        print(n+n-1)
    elif k == 4 * n - 4:
        print(n+n-2)
    else:
        print(n + n - 2 - (4 * n - 4 - k) // 2)

for t in range(int(input())):
    solve()