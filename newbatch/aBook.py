def solve():
    n = int(input())
    t = [[] for i in range(n+1)]
    per = [[] for i in range(n+1)]
    for i in range(n):
        t[i+1] = list(map(int, input().split()))
        for j in range(1, t[i+1][0]+1):
            per[t[i+1][j]].append(i+1)

    queue = []
    ans = [0] * (n+1)
    count = [0] * (n+1)

    for i in range(1, n+1):
        if len(t[i]) == 1:
            queue.append(i)
            ans[i] = 1

    while len(queue) != 0:
        cur = queue.pop()
        for par in per[cur]:
            count[par] += 1
            if par > cur:
                ans[par] = max(ans[par], ans[cur])
            else:
                ans[par] = max(ans[par], ans[cur] + 1)
            if count[par] >= t[par][0]:
                queue.append(par)
    # print("TEST")
    # print(t)
    # print(per)
    # print(count)
    for i in range(1, n+1):
        if count[i] < t[i][0]:
            print(-1)
            return
    print(max(ans))


for t in range(int(input())):
    solve()