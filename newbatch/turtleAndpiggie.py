def solve():
    l, r = map(int, input().split())

    start = 2
    ans = 0
    while start <= r:
        ans += 1
        start  = start * 2
    print(ans)
for t in range(int(input())):
    solve()