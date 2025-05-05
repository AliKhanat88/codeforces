from heapq import heappop, heappush

def solve():
    n,m,d = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sumi = 0
    heapi = []
    maxi = 0
    for i in range(n):
        if arr[i] > 0:
            if len(heapi) < m:
                sumi += arr[i]
                heappush(heapi, arr[i])
            else:
                temp = heappop(heapi)
                if temp < arr[i]:
                    sumi = sumi - temp
                    sumi += arr[i]
                    heappush(heapi, arr[i])
                else:
                    heappush(heapi, temp)
        maxi = max(maxi, sumi - d * (i+1))
        # print(heapi, sumi)
    print(maxi)

for t in range(int(input())):
    solve()