def solve():
    n, k = map(int, input().split())
    if k >= n-1:
        print(1)
    else:
        print(n)

for t in range(int(input())):
    solve()