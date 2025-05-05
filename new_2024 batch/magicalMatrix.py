def solve():
    n = int(input())
    sumi = 0
    for i in range(n, -1, -1):
        sumi += ((i + i - 1) * i)

    print(sumi, 2 * n - 1)

    per = [i + 1 for i in range(n)]
    rev = [i for i in range(n, 0, -1)]
    print(1, 1, *per)   
    row = 2
    for i in range(n-1, 0, -1):
        print(2, i, *rev)
        print(1, row, *per)
        row += 1


for t in range(int(input())):
    solve()