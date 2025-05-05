def solve():
    n, m = map(int, input().split())
    graph = [set() for i in range(n+1)]

    for i in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)


    visited = [False] * (n+1)
    cur_path = [0]
    stack = [(0, 1)]
    while len(stack) != 0:
        cur = stack.pop()
        while cur_path[-1] != cur[0]:
            temp = cur_path.pop()
            visited[temp] = False
        if visited[cur[1]] == True:
            print(cur_path, cur[1])
            temp_set = set()
            temp_set.add(cur[1])
            i = len(cur_path) - 1
            while i > -1:
                if cur_path[i] == cur[1]:
                    break
                temp_set.add(cur_path[i])
                i -= 1
            edges = []
            for child in graph[cur[1]]:
                if child not in temp_set:
                    edges.append(child)
            if len(edges) > 1:
                ans = []
                ans.append((cur[1], edges[0]))
                ans.append((cur[1], edges[1]))
                per = cur[1]
                i = len(cur_path) - 1
                while i > -1:
                    if cur_path[i] == cur[1]:
                        break
                    ans.append((cur_path[i], per))
                    per = cur_path[i]
                    i -= 1
                ans.append((cur[1], per))
                print("YES")
                print(len(ans))
                for edge in ans:
                    print(*edge)
                return
                
            # input()
            # print(stack)
            continue
        cur_path.append(cur[1])

        visited[cur[1]] = True
        for children in graph[cur[1]]:
            if children != cur[0]:
                stack.append((cur[1], children))
        
    print("NO")


for t in range(int(input())):
    solve()