def solve():
    n, m = map(int, input().split())
    print(n * m)
    k = -256
    for i in range(n):
        k = k + 256
        for j in range(m):
            print(k + j, end= " ")
        print()
for t in range(int(input())):
    solve()