import sys
input = sys.stdin.readline
from collections import defaultdict
from bisect import bisect_left, bisect_right

def solve():
    n, q = map(int, input().split())
    dict = {
        "U": 1,
        "D": -1,
        "L": -1,
        "R": 1
    }
    s = input()
    forward = defaultdict(lambda: [])
    backward = defaultdict(lambda: [])
    state_forward = [[0, 0] for i in range(n+2)]
    state_backward = [[0, 0] for i in range(n+2)]
    hor = 0
    ver = 0
    for i in range(n):
        if s[i] == "U" or s[i] == "D":
            ver += dict[s[i]]
        else:
            hor += dict[s[i]]
        forward[ver].append((hor, i+1))
        state_forward[i+1] = [ver, hor]
    hor, ver = 0, 0
    for i in range(n-1, -1, -1):
        if s[i] == "U" or s[i] == "D":
            ver += dict[s[i]]
        else:
            hor += dict[s[i]]
        backward[ver].append((hor, i+1))
        state_backward[i+1] = [ver, hor]
    forward[0].append((0, 0))
    backward[0].append((0, 0))
    # print(forward)
    # print(state_forward)
    # print(backward)
    # print(state_backward)
    for key in backward:
        backward[key].sort()
    for key in forward:
        forward[key].sort()

    
    for i in range(q):
        x, y, l, r = map(int, input().split())
        temp = bisect_right(forward[y], (x, l-1))
        if temp > 0 and forward[y][temp-1][0] == x:
            print("YES")
            continue
        temp = bisect_left(forward[y], (x, r))
        if temp < len(forward[y]) and forward[y][temp][0] == x:
            print("YES")
            continue
        y = y - state_forward[l-1][0] + state_backward[r+1][0]
        x = x - state_forward[l-1][1] + state_backward[r+1][1]
        temp = bisect_right(backward[y], (x, l-1))
        if temp < len(backward[y]) and backward[y][temp][0] == x and backward[y][temp][1] <= r:
            print("YES")
            continue
        print("NO")
        

    




solve()