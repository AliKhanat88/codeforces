for t in range(int(input())):
    n, s1, s2, d1, d2 = map(int, input().split())
    if s1 > n // 2:
        s1 = n - s1 + 1
    if s2 > n // 2:
        s2 = n - s2 + 1
    if d1 > n // 2:
        d1 = n - d1 + 1
    if d2 > n // 2:
        d2 = n - d2 + 1
    print(abs(min(s1, s2) - min(d1, d2)))
    