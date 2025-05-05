from heapq import heappush, heappop
def solve():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if k == 0:
        sumi = 0
        for i in range(n):
            if a[i] < b[i]:
                sumi += (b[i] - a[i])
        print(sumi)
        return
    points = [(a[i], b[i]) for i in range(n)]
    points.sort(key=lambda x: x[1], reverse=True)
    # print(points)

    suffix = [0] * (n+1)
    for i in range(n-1, -1, -1):
        if points[i][1] >= points[i][0]:
            suffix[i] = suffix[i+1] + points[i][1] - points[i][0]
        else:
            suffix[i] = suffix[i+1]

    heapi = []
    maxi = 0
    sumi_t = 0
    for i in range(k):
        heappush(heapi, -points[i][0])
        sumi_t += points[i][0]
    # print(suffix)
    maxi = max(maxi, suffix[k] - sumi_t)
    for i in range(k, n):
        # print(heapi)
        # print(points[i])
        if abs(heapi[0]) > points[i][0]:
            temp = heappop(heapi)
            heappush(heapi, -points[i][0])
            sumi_t += points[i][0]
            sumi_t += temp
        maxi = max(maxi, suffix[i+1] - sumi_t)

    print(maxi)
for t in range(int(input())):
    solve()