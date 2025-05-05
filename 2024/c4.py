from heapq import heappop, heappush
from collections import Counter

def solve():
    n = int(input())
    arr = list(list(input().strip()))
    c = Counter(arr)
    heap = []
    for key, val in c.items():
        heappush(heap, (-val, key))
    ans= []
    while len(heap) > 1:
        temp1 = heappop(heap)
        temp2 = heappop(heap)
        ans.append(temp1[1])
        ans.append(temp2[1])
        if -temp1[0] - 1 > 0:
            heappush(heap, (temp1[0] + 1, temp1[1]))
        if -temp2[0] - 1 > 0:
            heappush(heap, (temp2[0] + 1, temp2[1]))
    if len(heap) == 1:
        for num in range(-heap[0][0]):
            ans.append(heap[0][1])
    print("".join(ans))
for t in range(int(input())):
    solve()