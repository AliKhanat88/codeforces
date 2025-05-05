def cal_z_function(s):
    n = len(s)
    z_fun = [0] * n
    z_fun[0] = n
    l, r = 0, 0

    for i in range(1, n):
        if i < r:
            z_fun[i] = min(z_fun[i - l], r - i + 1)

        while i + z_fun[i] < n and s[i + z_fun[i]] == s[z_fun[i]]:
            z_fun[i] += 1
        if i + z_fun[i] - 1 > r:
            l, r = i, i + z_fun[i] - 1
    return z_fun

import sys
input = sys.stdin.readline


def solve():
    n, k, r = map(int, input().split())

    s = input().strip()

    z = cal_z_function(s)

    # print(z)

    def check(length):
        count = 0
        i = 0
        while i < n:
            if z[i] >= length:
                i += length
                count += 1
            else:
                i += 1
        return count

    l = 1
    r = n
    
    while l + 1 < r:
        # print(l, r)
        m = (l + r) // 2
        temp = check(m)
        if temp >= k:
            l = m
        else:
            r = m - 1
    if check(r) >= k:
        print(r)
    elif check(l) >= k:
        print(l)
    else:
        print(0)



for t in range(int(input())):
    solve()