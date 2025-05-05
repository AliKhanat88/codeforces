from collections import defaultdict
from math import ceil

def solve():
    n = int(input())
    a = input().split()
    dict = defaultdict(lambda:0)

    for num in a:
        dict[num] += 1

    a = 0
    b = 0
    reverse = False
    ans = 0
    for num, count in dict.items():
        if count == 1:
            ans += 1
        elif count % 2 == 0:
            a += 1
            b += 1
        else:
            if reverse:
                
                reverse = False
            else:
                reverse = True
            b += 1
            a += 1
    if reverse == True:
        print(a + ceil(ans / 2))
    else:
        print(a + ceil(ans / 2))


for t in range(int(input())):
    solve()