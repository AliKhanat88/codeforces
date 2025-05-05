from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def find_central_node(graph, n):
    
    def dijkstra(start_node, total_nodes):
        distances = [float('inf')] * (total_nodes + 1)
        distances[start_node] = 0
        min_heap = [(0, start_node)]

        while min_heap:
            current_distance, current_node = heappop(min_heap)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heappush(min_heap, (distances[neighbor], neighbor))
        print(distances)
        return sum(distances[1:])

    optimal_node = None
    min_distance_sum = float('inf')

    for node in range(1, n + 1):
        total_distance = dijkstra(node, n)
        if total_distance < min_distance_sum:
            min_distance_sum = total_distance
            optimal_node = node

    print(optimal_node)


for _ in range(int(input())):
    n, m= map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n):
        node1, node2, weight = map(int, input().split())
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))

    find_central_node(graph, n)
