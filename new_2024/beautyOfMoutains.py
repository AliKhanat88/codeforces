import sys
input = sys.stdin.readline
from math import gcd

def solve():
    n, m, k = map(int, input().strip().split())
    arr = [0] * n
    total = 0
    for i in range(n):
        arr[i] = list(map(int, input().strip().split()))
    
    bin = [0] * n
    for i in range(n):
        bin[i] = list(map(int, list(input().strip())))
        for j in range(m):
            if bin[i][j] == 1:
                total += arr[i][j]
            else:
                total -= arr[i][j]
    
    data = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        sumi = sum(bin[i][:k])
        data[i][k-1] = sumi
        for j in range(k, m):
            sumi -= bin[i][j-k]
            sumi += bin[i][j]
            data[i][j] = sumi
    
    # print(data)
    g = 0
    for i in range(k-1, m):
        sumi = 0
        for j in range(k):
            sumi += data[j][i]
        # print("pair", k * k - sumi,  sumi)
        g = gcd(g, abs(k * k - sumi - sumi))
        for j in range(k, n):
            sumi -= data[j-k][i]
            sumi += data[j][i]
            # print("pair", k * k - sumi,  sumi)
            g = gcd(g, abs(k * k - sumi - sumi))
    # print(total, g)
    if g == 0 and total == 0:
        print("YES")
    elif g == 0 and total != 0:
        print("NO")
    elif total % g == 0:
        print("YES")
    else:
        print("NO")



for t in range(int(input())):
    solve()