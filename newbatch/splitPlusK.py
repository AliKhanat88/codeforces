from math import gcd

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    gc = arr[0] - k
    for i in range(n):
        if arr[i] - k == 0:
            for j in range(n):
                if arr[j] != k:
                    print(-1)
                    return
            print(0)
            return
        gc = gcd(gc, arr[i] - k)
    gc = gcd(*[arr[i]-k for i in range(n)])
    # print(gc)
    ans = 0
    above = 0
    for i in range(n):
        if arr[i] > k:
            above += 1
        temp = abs((arr[i] - k) // gc)
        if (arr[i] + (temp - 1) * k) % temp != 0:
            print(-1)
            return
        ans += abs(temp) - 1
    if above == n or above == 0:
        print(ans)
    else:
        print(-1)


for t in range(int(input())):
    solve()