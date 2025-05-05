from collections import defaultdict

import heapq
inf = 99999999999999999999999
def dijkstra(graph, start, dist, dist_have, n, horses):
    
    # Distance array, initialized with infinity for all nodes except the start node
    dist[start] = 0
    
    # Priority queue to store the vertices to explore
    pq = [(0, start, False)]  # (distance, vertex)

    
    while pq:
        # Get the node with the smallest distance
        current_dist, u, have_horse = heapq.heappop(pq)
        if u in horses or have_horse == True:
            can = True
        else:
            can = False
        # If the current distance is greater than the stored one, we continue (this node was already processed)
        if can == False:
            if current_dist > dist[u]:
                continue
            
            # Explore neighbors
            for neighbor, weight in graph[u]:
                distance = current_dist + weight
            
                
                # If a shorter path is found
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor, can))
        else:
            if current_dist > dist_have[u]:
                continue
            
            # Explore neighbors
            for neighbor, weight in graph[u]:
                distance = current_dist + weight // 2
            
                
                # If a shorter path is found
                if distance < dist_have[neighbor]:
                    dist_have[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor, can))


def solve():
    n, m, h = map(int, input().split())
    horses = set(map(int, input().split()))

    graph = defaultdict(lambda:[])
    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    # print(graph)
    dist1 = [inf] * (n + 1)
    dist1_have = [inf] * (n + 1)
    dijkstra(graph, 1, dist1, dist1_have, n, horses)
    # print(dist1)
    # print(dist1_have)
    dist2 = [inf] * (n + 1)
    dist2_have = [inf] * (n + 1)
    dijkstra(graph, n, dist2,dist2_have, n, horses)
    # print(dist2)
    mini = inf
    for i in range(1, n+1):
        mini = min(mini, max(min(dist1[i], dist1_have[i]), min(dist2[i], dist2_have[i])))
    if mini == inf:
        print(-1)
    else:
        print(mini)
for t in range(int(input())):
    solve()