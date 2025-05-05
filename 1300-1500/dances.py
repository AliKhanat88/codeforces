def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [0] + a

    a.sort()
    b.sort()
    i = n-1
    ans = 0
    last = -1
    while i >= 0:
        if b[i] <= a[i]:
            b.pop(0)
            a.pop(-1)
            ans += 1
        i -= 1
    print(ans)


for t in range(int(input())):
    solve()