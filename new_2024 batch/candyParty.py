from collections import defaultdict
from math import log2

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    dict = defaultdict(lambda:0)

    temp = sum(arr)

    if temp % n != 0:
        print("NO")
        return
    temp = temp // n
    for num in arr:
        if num == temp:
            continue
        i = 1
        found = False
        while i <= 2 ** 30:
            # print(temp, num, i)
            if (temp - num + i) > 0 and log2(temp - num + i) % 1 == 0:
                found = True
                dict[i] += 1
                dict[temp - num + i] -= 1
                break
            i = i * 2
        if found == False:
            print("NO")
            return
    
    for key, val in dict.items():
        if val != 0:
            print("NO")
            return
    print("YES")
for t in range(int(input())):
    solve()

