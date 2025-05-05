
def solve():
    n = int(input())
    parent_tree = list(map(int, input().split()))
    parent_tree = [-1, -1] + parent_tree
    graph = [[] for i in range(n+1)]

    for i in range(2, n+1):
        graph[parent_tree[i]].append(i)

    # # topological sort
    top_sort_tree = [0] * (n+1)
    index = 1
    top = 1
    queue = [(top, -1)]

    while len(queue) != 0:
        new_queue = []
        for i in range(len(queue)):
            for child in graph[queue[i][0]]:
                new_queue.append((child, index))
            top_sort_tree[index] = (queue[i][1], queue[i][0])
            index += 1
        queue = new_queue
    # print(graph)
    # print(top_sort_tree)

    counts = [[] for i in range(n+1)]
    for i in range(n, 1, -1):
        if len(counts[i]) == 0:
            counts[top_sort_tree[i][0]].append((1, 0))
        elif len(counts[i]) == 1:
            counts[top_sort_tree[i][0]].append((counts[i][0][0]+1, counts[i][0][1]))
        else:
            sumi = 0
            temp_maxi = -1
            for j in range(len(counts[i])):
                temp_maxi= max(temp_maxi, counts[i][j][0])
                sumi = sumi + max(counts[i][j][0], counts[i][j][1])
            counts[top_sort_tree[i][0]].append((temp_maxi + 1, sumi))
    # print(counts)
    sumi = 0
    temp_maxi = -1
    for j in range(len(counts[1])):
        temp_maxi= max(temp_maxi, counts[1][j][0])
        sumi = sumi + max(counts[1][j][0], counts[1][j][1])
    print(max(sumi, temp_maxi + 1))

# for t in range(int(input())):
solve()