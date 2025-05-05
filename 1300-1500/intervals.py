import sys
input = sys.stdin.readline
from bisect import bisect_right
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    intervals = [0] * m
    dict = defaultdict(lambda: True)
    for i in range(m):
        temp = (*map(int, input().split()),)
        if dict[temp]:
            intervals[i] = temp
            dict[intervals[i]] = False

    for i in range(m-1, -1, -1):
        if intervals[i] == 0:
            intervals.pop(i)

    dict = defaultdict(lambda: 0)
    intervals = sorted(intervals, key=lambda x: x[0])


    c = int(input())
    for i in range(1, c+1):
        chan = int(input())
        for j in range(bisect_right(intervals, (chan, 999999))):
            if intervals[j][1] >= chan:
                if dict[intervals[j]] >= (intervals[j][1] - intervals[j][0] + 1) // 2:
                    for k in range(i+1, c+1):
                        input()
                    print(i)
                    return
                else:
                    dict[intervals[j]] += 1
    print(-1)

for t in range(int(input())):
    solve()