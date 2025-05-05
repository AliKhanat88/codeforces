import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n, m = map(int,input().split())
    dictFirst = defaultdict(lambda:0)
    dictLast = defaultdict(lambda:0)

    for i in range(n):
        a, b = map(int, input().split())

        if a != 1:
            dictFirst[a] += 1
            dictFirst[b+1] -= 1
        if b != m:
            dictLast[a] += 1
            dictLast[b+1] -= 1
    
    pairs1 = sorted(dictFirst.items(), key=lambda x: x[0])
    pairs2 = sorted(dictLast.items(), key=lambda x:x[0])

    # print("TEST")
    # print(pairs1)
    # print(pairs2)
    maxi1 = 0
    sumi = 0
    for num in pairs1:
        sumi += num[1]
        maxi1 = max(maxi1, sumi)

    maxi2 = 0
    sumi = 0
    for num in pairs2:
        sumi += num[1]
        maxi2 = max(maxi2, sumi)

    print(max(maxi1, maxi2))



for t in range(int(input())):
    solve()