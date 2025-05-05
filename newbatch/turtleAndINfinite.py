def solve():
    n, m = map(int, input().split())
    l = max(0, n - m)
    r = n+m
    ans = 0
    for b in range(31):
        temp = b+1
        if (l % (2 ** temp)) == 0:
            # print(l + 2 ** (temp-1), 2 ** temp)
            if l + 2 ** (temp-1) <= r:
                ans += (2 ** b)
        else:
            mult = l // (2 ** temp) * (2 ** temp)
            if mult + 2 ** (temp-1) <= r:
                ans += (2 ** b)
    print(ans)

for t in range(int(input())):
    solve()