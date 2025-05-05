import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    mini = n - c[1]
    # print(mini)
    for num in arr:
        if num != 1:
            maxi = c[num]
            sumi = c[num]
            for x in range(num + num, n+1, num):
                maxi = max(maxi, c[x])
                sumi += c[x]
            # print(sumi,num, maxi)
            mini = min(mini, sumi - maxi + c[1] + (n - sumi - c[1]) * 2)
    print(mini)
for t in range(int(input())):
    solve()