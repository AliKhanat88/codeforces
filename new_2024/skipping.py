from heapq import heappop, heappush

def solve():
    n = int(input())
    inf = 99999999999999999999999999999999999999
    arr = list(map(int, input().split()))
    brr = list(map(int ,input().split()))
    ans = arr[0]
    heap = [(arr[0], brr[0]-1)]
    sumi = 0
    for i in range(n):
        sumi += arr[i]
        while len(heap) > 0:
            if heap[0][1] < i:
                heappop(heap)
            else:
                break
        temp = inf
        if len(heap):
            temp = min(temp, heap[0][0])
        ans = max(ans, sumi - temp)
        if brr[i] - 1 >= i:
            heappush(heap, (temp + arr[i], brr[i]-1))
    print(ans)

for t in range(int(input())):
    solve()