def solve():
    n, k = map(int, input().split())
    ans = [0]
    while True:
        if sum(ans) + 1 == k:
            break
        if 2 * sum(ans) + 1 >= k:
            ans.append(k - sum(ans) - 1)
        else:
            ans.append(sum(ans) + 1)
    # print(ans)
    while len(ans) < 25:
        temp = sum(ans)+1
        ans.append(temp)
        ans.append(temp + k)
    ans.append(k+1)
    print(len(ans) - 1)
    print(*sorted(ans[1:]))


for t in range(int(input())):
    solve()