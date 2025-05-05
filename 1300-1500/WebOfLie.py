import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n, f = map(int, input().split())
    dict = defaultdict(lambda:0)
    for i in range(f):
        a, b = map(int, input().split())
        dict[min(a,b)] += 1
    
    q = int(input())
    for i in range(q):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            dict[min(arr[1], arr[2])] += 1
        elif arr[0] == 2:
            temp = min(arr[1], arr[2])
            dict[temp] -= 1
            if dict[temp] == 0:
                del(dict[temp])
        else:
            print(n - len(dict))

solve()