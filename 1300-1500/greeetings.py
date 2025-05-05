import sys
input = sys.stdin.readline
from bisect import bisect_left


def solve():
    n = int(input())
    a = [0] * n
    b = [0] * n
    index = [i for i in range(n)]
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    
    index.sort(key=lambda i:a[i])
    ans = 0
    add_ele = []
    # print(a)
    # print(b)
    # print(index)
    for i in range(n):
        temp = bisect_left(add_ele, b[index[i]])
        ans += len(add_ele) - temp
        add_ele.insert(temp, b[index[i]])
    print(ans)
for t in range(int(input())):
    solve()