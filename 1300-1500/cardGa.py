from math import comb

def solve():
    n = int(input())
    done = True
    a = 0
    b = 0
    while n > 2:
        if done == True:
            done = False
            a += comb(n-1, n // 2 -1)
            b += comb(n - 2, n // 2 - 2)
        else:
            b += comb(n-1, n // 2 -1)
            a += comb(n - 2, n // 2 - 2)
            done = True
        n -= 2
    if done == True:
        a += 1
        b += 0
    else:
        b += 1
        a += 0
    print(a % 998244353, b % 998244353, 1 % 998244353)

for t in range(int(input())):
    solve()               