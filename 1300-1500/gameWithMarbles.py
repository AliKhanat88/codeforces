def solve():
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]

    index = [i for i in range(n)]

    index.sort(key=lambda x: a[x]+b[x], reverse=True)
    # print(index)
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += (a[index[i]] - 1)
        else:
            ans -= (b[index[i]] - 1)
        # print(ans)
    print(ans)
for t in range(int(input())):
    solve()