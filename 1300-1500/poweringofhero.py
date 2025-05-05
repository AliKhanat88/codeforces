from heapq import heappush, heappop

def solve():
    n = int(input())
    arr = [-int(num) for num in input().split()]
    heap = []
    ans = 0
    for i in range(n):
        if arr[i] == 0:
            if len(heap) > 0:
                ans -= heappop(heap)
                #///
        else:
            heappush(heap, arr[i])
    print(ans)
for t in range(int(input())):
    solve()