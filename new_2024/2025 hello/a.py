def solve():
    n, m = map(int, input().split())
    print(max(n, m) + 1)


for t in range(int(input())):
    solve()