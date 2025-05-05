def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] - b[i] for i in range(n)]
    maxi = max(c)
    s = []
    for i in range(n):
        if c[i] == maxi:
            s.append(str(i+1))
    print(len(s))
    print(" ".join(s))


for t in range(int(input())):
    solve()

