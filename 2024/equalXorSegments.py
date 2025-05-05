import sys
input = sys.stdin.readline
from collections import defaultdict
from bisect import bisect_left

def solve():
    n , q = map(int, input().split())

    arr = list(map(int, input().split()))
    
    dict = defaultdict(lambda: [])
    sumi = [0] * (n + 1)
    for i in range(1, n+1):
        sumi[i] = sumi[i-1] ^ arr[i-1]
        dict[sumi[i]].append(i)

    # print(sumi)
    # print(dict)

    for i in range(q):
        l, r = map(int, input().split())
        last = sumi[r] ^ sumi[l-1]
        # print(l, r, last, 0 ^ sumi[l-1], last ^ sumi[l-1])
        if last == 0:
            print("YES")
        else:
            ind = bisect_left(dict[0 ^ sumi[l-1]], r) - 1
            if ind < 0:
                print("NO")
            else:
                ind_0 = dict[0 ^ sumi[l-1]][ind]
                ind = bisect_left(dict[last ^ sumi[l-1]], ind_0) - 1
                if ind < 0 :
                    print("NO")
                else:
                    if dict[last ^ sumi[l-1]][ind] >= l:
                        print("YES")
                    else:
                        print("NO")
                # if ind <= l:
    print()


for t in range(int(input())):
    solve()