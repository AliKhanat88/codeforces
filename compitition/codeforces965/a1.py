def solve():
    a, b, k = map(int, input().split())
    if a <= k:
        n = a
    else:
        n = k
    if b <= k:
        m = b
    else:
        m = k
    print(n * m)

for t in range(int(input())):
    solve()