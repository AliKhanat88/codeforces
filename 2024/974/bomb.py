from heapq import heappop, heappush

def solve():
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))


    def check(x):

        tempk = 0
        ans = 0
        heap = []
        for i in range(n):
            oper = max(0, arr[i] - x) // brr[i]
            if max(0, arr[i] - x) % brr[i] != 0:
                oper += 1
            tempk += oper
            ans += arr[i] * oper - (((oper) * (oper - 1)) // 2) * brr[i]
            heappush(heap, -max(0, arr[i] - brr[i] * oper))
        for i in range(n):
            if k - tempk > 0:
                ans -= heappop(heap)
                tempk += 1
        return ans, tempk
    l = 0 
    r = 10 ** 9 
    while l + 1 < r:
        m = (l + r) // 2
        ans, tempk = check(m)
        if tempk <= k:
            r = m
        else:
            l = m + 1
        # print(tempk, m, ans)
    ans, tempk = check(l)
    if tempk <= k:
        print(ans)
        return 
    ans, tempk = check(r)
    print(ans)

for t in range(int(input())):
    solve()