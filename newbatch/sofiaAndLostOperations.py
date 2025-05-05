import sys
input = sys.stdin.readline
from collections import Counter, defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    m = int(input())
    crr = list(map(int, input().split()))
    dict = defaultdict(lambda:-1)
    # print("TEST")
    for i in range(m):
        dict[crr[i]] = i


    c = Counter(crr)
    maxi = -1
    for i in range(n):
        if arr[i] != brr[i]:
            if c[brr[i]] >= 1:
                c[brr[i]] -= 1
            else:
                print("NO")
                return
        maxi = max(maxi, dict[brr[i]])
    if maxi >= m - 1:

        print("YES")
    else:
        print("NO")


for t in range(int(input())):
    solve()