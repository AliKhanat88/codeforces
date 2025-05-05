from collections import defaultdict
from math import ceil
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    mini = arr[-1]
    for i in range(n-2, -1, -1):
        if (arr[i] / mini) % 1 == 0:
            x = arr[i] // mini 
        else:
            x = arr[i] // mini + 1
        ans += x - 1
        mini = arr[i] // x
        

    print(ans)
for t in range(int(input())):
    solve()