def solve():
    n = int(input())

    p_a, p_b = map(int, input().split())

    graph = [[] for i in range(n+1)]

    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    if n == 1:
        print(0)
        return
    visited = [0] * (n+1)
    stack_a = [(p_a, 0)]
    stack_b = [(p_b, 0)]
    result = None
    while len(stack_a) != 0 and len(stack_b) != 0:
        next_level_a = []

        # Pop all elements from the stack for the current level
        for node in stack_a:
            if visited[node[0]] == 0:
                visited[node[0]] = 1
                for neighbor in graph[node[0]]:
                    next_level_a.append((neighbor, node[1] + 1))

        # Reverse next_level to maintain order when pushed onto stack
        stack_a = next_level_a

        next_level_b = []

        # Pop all elements from the stack for the current level
        for node in stack_b:
            if visited[node[0]] == 0:
                visited[node[0]] = 2
                for neighbor in graph[node[0]]:
                    next_level_b.append((neighbor, node[1] + 1))
            elif visited[node[0]] == 1:
                 result = node
                 break
        if result != None:
            break

        # Reverse next_level to maintain order when pushed onto stack
        stack_b = next_level_b
    
    # print(result)
    ans = result[1]
    # print(graph)
    # topological sort
    top_sort_tree = [0] * (n+1)
    index = 1
    visited = [False] * (n+1)
    queue = [(result[0], -1)]

    while len(queue) != 0:
        new_queue = []
        for i in range(len(queue)):
            for child in graph[queue[i][0]]:
                visited[queue[i][0]] = True
                if not visited[child]:
                    new_queue.append((child, index))
            top_sort_tree[index] = (queue[i][1], queue[i][0])
            index += 1
        queue = new_queue
    # print(top_sort_tree)

    op = [[] for i in range(n+1)]

    for i in range(n, 1, -1):
        if len(op[i]) == 0:
            op[top_sort_tree[i][0]].append((1, 1))
        else:
            maxi = -1
            sumi = 0
            for tup in op[i]:
                maxi = max(maxi, tup[1])
                sumi = sumi + tup[0]
            op[top_sort_tree[i][0]].append((sumi+1, maxi+1))
    maxi = -1
    sumi = 0
    for tup in op[1]:
        maxi = max(maxi, tup[1])
        sumi = sumi + tup[0] * 2

    print(sumi - maxi + ans)
    
    # print(op)

for t in range(int(input())):
    solve()