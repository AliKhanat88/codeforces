from collections import defaultdict
from bisect import bisect_left, bisect_right

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dict = defaultdict(lambda:[])
    for i, num in enumerate(arr):
        dict[num].append(i)
    sorted_item = sorted(dict.items(), key=lambda x: x[1][-1] - x[1][0], reverse=True)
    sumi = 0
    per = sorted_item[0][1][0]
    last = sorted_item[0][1][-1]
    if sorted_item[0][1][-1] - sorted_item[0][1][0] == 0:
        print(0)
        return
    for i in range(1, len(sorted_item)):
        left = bisect_right(sorted_item[i][1], per)
        if left != 0:
            
        right = bisect_left(sorted_item[i][1], last)
            
    print(sorted_item)
    # print(sumi)


for t in range(int(input())):
    solve()