def solve():
    n, m = map(int, input().split())
    ans = 0
    while m > n:
        if m % 2 == 1:
            m += 1
            ans += 1
        else:
            m = m // 2
            ans += 1
    ans += (n - m)
    print(ans)


solve()