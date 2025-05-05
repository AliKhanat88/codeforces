def solve():
    n, m = map(int, input().split())
    adj = [set() for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())

        adj[a].add(b)
        adj[b].add(a)
    
    
    # double = []
    # print(adj)
    ans = []
    for i in range(1, n+1):
        temp_childs = list(adj[i])
        for child in temp_childs:
            if child in adj[i] and len(adj[child]) > 1:
                adj[child].remove(i)
                adj[i].remove(child)
                temp = adj[child].pop()
                adj[temp].remove(child)
                if temp not in adj[i]:
                    adj[i].add(temp)
                    adj[temp].add(i)
                    temp_childs.append(temp)
                else:
                    adj[i].remove(temp)
                    adj[temp].remove(i)
                    # temp_childs.append(temp)
                ans.append((i, child, temp))
    double = []
    
    # print(adj)
    
    for i in range(1, n+1):
        assert len(adj[i]) <= 1
        if len(adj[i]) == 1:
            temp = adj[i].pop()
            double.append((i, temp))
            adj[temp].remove(i)
    # print(double)
    # print(ans)
    if len(double) != 0:
        # print(double)
        visited = [False] * (n+1)
        visited[double[0][0]] = True
        visited[double[0][1]] = True
        for i in range(1, len(double)):
            ans.append((double[i-1][0], double[i-1][1], double[i][0]))
            visited[double[i][0]] = True
            visited[double[i][1]] = True
        cur0 = double[-1][0]
        cur1 = double[-1][1]
        for i in range(1, n+1):
            if not visited[i]:
                ans.append((cur0, cur1, i))
                cur0 = i
    print(len(ans))
    for tup in ans:
        print(*tup)
    




for t in range(int(input())):
    solve()