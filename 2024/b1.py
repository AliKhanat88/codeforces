def solve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ans = 0
    if a > c:
        l = a
        ans += 1
    elif c > a:
        l = c
        ans += 1
    else:
        l = a
    if b > d:
        r = d
        ans += 1
    elif d > b:
        r = b
        ans += 1
    else:
        r = b
    ans += (r - l)
    print(max(1, ans))

for t in range(int(input())):
    solve()