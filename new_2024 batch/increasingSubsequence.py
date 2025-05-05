def solve():
    n = int(input())
    i = 65
    ans = []
    while n < 2 ** i:
        i -= 1
    max = 200
    for j in range(max - i, max):
        ans.append(j)
    n = n - 2 ** i
    max = max - i

    while n != 0:
        i = 65
        while n < 2 ** i:
            i -= 1
        ans.append(ans[i])
        n = n - (2 ** i)
    print(len(ans))
    print(*ans)


for t in range(int(input())):
    solve()