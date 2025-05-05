def solve():
    n, k = map(int, input().split())

    ans = []
    temp_k = 0
    first = 1
    last = n
    while len(ans) < n:
        if temp_k == k - 1:
            ans.append(first)
            temp_k = 0
            first += 1
        else:
            ans.append(last)
            last -= 1
            temp_k += 1
    print(*ans)

for t in range(int(input())):
    solve()