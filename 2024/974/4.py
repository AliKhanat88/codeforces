import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def solve():
    n, d, k = map(int, input().split())
    arr = []
    for i in range(k):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()
    # print(arr)
    
    points = [0] * ( n-d+2)
    heap = []
    j = 0
    count = 0
    for i in range(1, n-d+2):
        while j < k and i + d - 1 >= arr[j][0]:
            count += 1
            heappush(heap, arr[j][1])
            j += 1
        while len(heap) > 0 and heap[0] < i:
            count -= 1
            heappop(heap)
        points[i] = count
        # print(heap)
    points.pop(0)
    # print(points)
    print(points.index(max(points)) + 1, points.index(min(points)) + 1)

    
for t in range(int(input())):
    solve()