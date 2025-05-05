from heapq import *

def solve():
    n,m,x = map(int, input().split())
    arr = list(map(int, input().split()))

    heap = [(0, num) for num in range(1, m+1)]
    print("YES")
    for i in range(n):
        mini = heappop(heap)
        print(mini[1], end=" ")
        mini = (mini[0]+arr[i], mini[1])
        heappush(heap, mini)

    print()



for t in range(int(input())):
    solve()