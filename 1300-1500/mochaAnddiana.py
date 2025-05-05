from collections import defaultdict
from copy import deepcopy

def traverse(graph, node, visited):
    queue = [node]
    new_visited = defaultdict(lambda:-1)
    while len(queue) != 0:
        cur = queue.pop(0)
        if visited[cur] == 0:
            continue
        new_visited[cur] = 0
        visited[cur] = 0
        queue += graph[cur]
    return new_visited
    
def solve():
    n, m1, m2 = map(int, input().split())
    graph1 = defaultdict(lambda:[])
    graph2 = defaultdict(lambda:[])
    for i in range(m1):
        a, b = map(int, input().split())
        graph1[a].append(b)
        graph1[b].append(a)
    for i in range(m2):
        a, b = map(int, input().split())
        graph2[a].append(b)
        graph2[b].append(a)
    # if m1 > m2:
    #     graph1, graph2 = graph2, graph1
    visited = [-1] * (n+1)
    first_batch = list(traverse(graph2, 1, visited).keys())
    all_nodes = defaultdict(lambda:set())
    for num in first_batch:
        check(graph1, all_nodes, num)
    ans = []
    for i in range(1, n+1):
        if visited[i] == -1:
            new_batch = set(traverse(graph2, i, visited).keys())
            for key, val in all_nodes.items():
                diff = list(new_batch - val)
                if len(diff) > 0:
                    ans.append((key, diff[0]))
                    graph1[key].append(diff[0])
                    graph1[diff[0]].append(key)
                    nodes_to_add_1 = set(traverse(graph1, key, defaultdict(lambda: -1)).keys())
                    for node in nodes_to_add_1:
                        all_nodes[node] = all_nodes[node].union(nodes_to_add_1)
                    # print(all_nodes, new_batch, nodes_to_add_1, nodes_to_add_2, diff)
                    break
                    
            for num in new_batch:
                check(graph1, all_nodes, num)
            

    print(len(ans))
    for num in ans:
        print(num[0], num[1])



solve()