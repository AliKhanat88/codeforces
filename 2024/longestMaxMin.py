from heapq import heappop, heappush
from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dict = defaultdict(lambda: False)
    last = [False] * n
    for i in range(n-1, -1, -1):
        if dict[arr[i]] == False:
            last[i] = True
            dict[arr[i]] = True
    # print(last)


    heap_pos = []
    heap_neg = []

    visited = set()

    till = -1
    ans = []
    for i in range(n):
        if arr[i] not in visited:
            heappush(heap_pos, (arr[i], i))
            heappush(heap_neg, (-arr[i], i))
            if last[i]:
                while arr[i] not in visited:
                    if len(ans) % 2 == 1:
                        temp = heappop(heap_pos)
                    else:
                        temp = heappop(heap_neg)
                    if temp[1] <= till or abs(temp[0]) in visited:
                        continue
                    else:
                        ans.append(abs(temp[0]))
                        visited.add(abs(temp[0]))
                        till = temp[1]
        # print(ans, till)
        # print(heap_pos)
        # print(heap_neg)
    print(len(ans))
    print(*ans)
        
    

for t in range(int(input())):
    solve()