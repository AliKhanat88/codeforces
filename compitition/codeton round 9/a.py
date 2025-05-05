def solve():
    n = int(input())
    print(*[i +(i + 1) for i in range(n)])


for t in range(int(input())):
    solve()