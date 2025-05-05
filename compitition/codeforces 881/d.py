from collections import defaultdict

def sol():
    vertices = defaultdict(lambda:[])
    n = int(input())
    for i in range(n-1):
        a, b = map(int, input().split())
        vertices[a].append(b)
        vertices[b].append(a)

    graph = defaultdict(lambda:-1)
    # making graph
    queue = [1]
    count_leave = [0] * n
    i = 0
    while i < len(queue):
        cur = queue[i]
        for num in vertices[cur]:
            graph[num] = cur
            queue.append(num)
            vertices[num].remove(cur)
        if len(vertices[cur]) == 0:
            count_leave[cur-1] = 1
        i += 1
    for i in range(n-1, 0, -1):
        count_leave[graph[queue[i]] - 1] += count_leave[queue[i] -1]

    q = int(input())
    for i in range(q):
        a, b = map(int, input().split())
        print(count_leave[a-1] * count_leave[b-1])
        

for t in range(int(input())):
    sol()