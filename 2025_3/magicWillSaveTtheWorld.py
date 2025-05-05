from collections import Counter

def solve():
    w, f = map(int, input().split())

    n = int(input())
    arr = list(map(int, input().split()))

    sumi = sum(arr)

    dp = [0]*(sumi+1)

    dp[0] = 1

    for num in arr:
        for i in range(len(dp)-1, -1, -1):
            if dp[i] and i + num < len(dp):
                dp[i+num] = 1
    # print(dp)
    def can(num):
        nonlocal sumi
        one = min(sumi, num * w)
        two = min(sumi, num * f)
        # print(one, two)
        for i in range(one, -1, -1):
            if dp[i]:
                lowest = i
                break
        if two >= sumi - lowest:
            return True
        
        for i in range(two, -1, -1):
            if dp[i]:
                lowest = i
                break
        if one >= sumi - lowest:
            return True
        return False
    l = 0
    r = min(sumi // w + 1, sumi // f + 1)
    while l + 1 < r:
        m = (l + r) // 2
        if can(m):
            r = m
        else:
            l = m + 1
    # print(l, r)

    if can(l):
        print(l)
    else:
        print(r)
    # print(dp)
    # print(can(12))
    # print(sumi)

    
for t in range(int(input())):
    solve()