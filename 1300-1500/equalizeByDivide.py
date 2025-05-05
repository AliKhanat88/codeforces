from heapq import heapify,heappush, heappop
from math import ceil

def solve():
    n = int(input())
    arr = input().split()
    if len(set(arr)) == 1:
        print(0)
        return
    arr = [[int(arr[i]), i] for i in range(n)]
    heapify(arr)
    ans = []
    cur = heappop(arr)
    if cur[0] == 1:
        print(-1)
        return
    count = [cur]
    while len(arr) != 0:
        temp = heappop(arr)
        while temp[0] > cur[0]:
            ans.append(f"{temp[1]+1} {cur[1]+1}")
            temp[0] = ceil(temp[0] / cur[0])
        if temp[0] == cur[0]:
            count.append(temp)
        else:
            for point in count:
                heappush(arr, point)
            count = [temp]
            cur = temp
    print(len(ans))
    print("\n".join(ans))
            
for t in range(int(input())):
    solve()