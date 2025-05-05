from collections import defaultdict
from math import ceil, floor
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dict = defaultdict(lambda:0)
    sumi = 0
    for i in range(n):
        dict[arr[i]] += 1
        sumi += arr[i]
    
    queue = [0] * (n+5)
    queue[0] = sumi
    top = 0
    last = 1
    count = 0
    while top != last:
        cur = queue[top]
        top = (top + 1) % (n+5)
        count -= 1
        if dict[cur] > 0:
            dict[cur] -= 1
        elif (cur == 1 and dict[cur] <= 0) or count > n+1:
            print("NO")
            return
        else:
            queue[last] = ceil(cur / 2)
            last = (last + 1) % (n+5)
            queue[last] = floor(cur / 2)
            last = (last + 1) % (n+5)
            count += 2
        
        # print(dict)
        # print(queue)
    if sum(dict.values()) == 0:
        print("YES")
    else:
        print("NO")


for t in range(int(input())):
    solve()