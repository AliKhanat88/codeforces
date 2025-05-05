from math import isqrt


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    a, b = map(int, input().split())
    num = 300001
    lowest_Mult = [999999] * (num)

    for i in range(2, isqrt(num)+1):
        for j in range(i+i, num, i):
            lowest_Mult[j] = min(lowest_Mult[j], i, j // i)

    multiple = [set() for i in range(num)]

    for i in range(2, num):
        if lowest_Mult[i] == 999999:
            multiple[i].add(i)
        else:
            multiple[i].add(lowest_Mult[i])
            for x in multiple[i // lowest_Mult[i]]:
                multiple[i].add(x)
    # print(multiple)
    # print(num)
    graph = [set() for i in range(num)]
    # print(graph)
    for i, val in enumerate(arr):
        # print(i)
        # graph[val] = multiple[i]
        graph[val].add((val, i+1))
        for x in multiple[val]:
            for x1 in multiple[val]:
                graph[x].add((x1, i+1))
            graph[x].add((val, i+1))
            graph[val].add((x, i+1))

    # print(graph)

    del multiple
    del lowest_Mult

    visited = [False] * num

    queue = [((arr[a-1], -1), 0)]

    path_parent = [-1] * num
    if a == b:
        print(1)
        print(a)
        return
    if arr[a-1] == 1:
        print(-1) 
        return
    elif arr[a-1] == arr[b-1]:
        print(2)
        print(a, b)
        return
    path_parent[arr[a-1]] = (-1,a)
    while len(queue) != 0:
        new_queue = []
        for x in queue:
            if visited[x[0][0]] == False: 
                if x[0][1] == b:
                    # print(x[1])
                    # print(path_parent)
                    ans = []
                    temp = path_parent[x[0][0]]
                    while temp[1] != a:
                        ans.append(temp[1])
                        temp = path_parent[temp[0]]
                    ans.append(a)
                    print((len(ans)))
                    print(*reversed(ans))
                    return
                visited[x[0][0]] = True
                for y in graph[x[0][0]]:
                    if visited[y[0]] == False:
                        if path_parent[y[0]] == -1:
                            path_parent[y[0]] = (x[0][0], y[1])
                        new_queue.append((y, x[1]+1))
        queue = new_queue

    print(-1)
    # print(lowest_Mult)
    # print(multiple)





# for t in range(int(input())):
solve()