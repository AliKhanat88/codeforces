
def solve():
    n = int(input())
    adj = [[] for i in range(n+1)]

    for i in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # print(adj)
    childs = [len(adj[num]) for num in range(1, n+1)]
    childs.sort(reverse=True)
    maxi = 0
    for v in range(1, n+1):
        removes = []
        ans = len(adj[v])
        removes.append(ans)
        temp_maxi = -1
        for child in adj[v]:
            temp_maxi = max(temp_maxi, len(adj[child]) - 1)
            removes.append(len(adj[child]))
        removes.sort(reverse=True)
        done = False
        for i in range(len(removes)):
            if removes[i] != childs[i]:
                temp_maxi = max(temp_maxi, childs[i])
                done = True
                break
        if done == False and len(removes) < len(childs):
            temp_maxi = max(temp_maxi, childs[len(removes)])
        maxi = max(maxi, ans + temp_maxi - 1)
    print(maxi)



for t in range(int(input())):
    solve()