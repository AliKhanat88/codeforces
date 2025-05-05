def solve():
    n, m, r, c = map(int, input().split())
    # print(n * m - ((r-1) * m+c))
    # print(- (n - r - 1))
    print(n * m - ((r-1) * m+c) - (n - r) + (n - r) * m)

for t in range(int(input())):
    solve()