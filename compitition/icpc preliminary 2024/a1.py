from heapq import heappop, heappush



def solve(n, graph):

    def dik(node, n):
        distances = [float("inf") for i in range(n + 1)]
        ans = 0
        distances[node] = 0
        q = [(0, node)]
        
        while len(q) != 0:

            current_dist, current_node = heappop(q)

            if current_dist > distances[current_node]:
                continue
            ans += distances[current_node]
            for cur_neigb, w in graph[current_node]:
                distance = current_dist + w
                if distance < distances[cur_neigb]:
                    distances[cur_neigb] = distance
                    heappush(q, (distance, cur_neigb))
        # print(distances)
        return sum(distances[1:])
    

    last = 9999999999999999999999999999999
    ret = None
    for i in range(1, n+1):
        temp = dik(i, n)
        if temp < last:
            last = temp
            ret = i

    print(ret)
    

import sys
input = sys.stdin.readline


for t in range(int(input())):
    nodes, edges = map(int, input().split())
    
    graph = [[] for i in range(nodes + 1)]

    for i in range(edges):
        a, b,w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    solve(nodes ,graph)