def solve():
    n, s = map(int, input().split())

    if s % 2 != 0:
        print("NO")
        return
    req = s // 2
    p = [i for i in range(1, n+1)]
    can = n - 1
    lower = 0
    upper = n - 1

    while upper > lower:
        if req >= can:
            p[lower], p[upper] = p[upper], p[lower]
            lower += 1
            upper -= 1
            req -= can
            can -= 2
        else:
            lower += 1
            can -= 1
    if req == 0:
        print("YES")
        print(*p)
    else:
        print("NO")


for t in range(int(input())):
    solve()