from heapq import heappush, heappop
import sys

inf = float("inf")

def solve(n, adj):
    def dijkstra(start):
        dist = [inf] * (n + 1)
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            cur_dist, cur_node = heappop(heap)
            if cur_dist > dist[cur_node]:
                continue
            for neighbor, weight in adj[cur_node]:
                new_dist = cur_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(heap, (new_dist, neighbor))
        return dist

    # Precompute shortest distances from all nodes
    return [dijkstra(i) for i in range(1, n + 1)]


if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    adj = [[] for _ in range(road_nodes + 1)]
    total_weight = 0

    for _ in range(road_edges):
        u, v, w = map(int, input().rstrip().split())
        adj[u].append((v, w))
        assert w >= 0  # Ensure no negative weights
        total_weight += w

    # Precompute distances
    ans = solve(road_nodes, adj)

    # Process queries
    q = int(input().strip())
    for _ in range(q):
        x, y = map(int, input().split())
        distance = ans[x - 1][y]  # Convert 1-based to 0-based indexing
        if distance > total_weight:
            print(-1)
        else:
            print(distance)
