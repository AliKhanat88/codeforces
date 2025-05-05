def solve():
    n, k = map(int, input().split())
    data = [0] * n
    for i in range(n):
        data[i] = input()
    # print(data)
    for i in range(0, n, k):
        for j in range(0, n, k):
            # print(i, j)
            print(data[i][j], end="")
        print()

for t in range(int(input())):
    solve()