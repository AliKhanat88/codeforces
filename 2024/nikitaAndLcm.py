import sys
input = sys.stdin.readline
from math import lcm 
from math import isqrt

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    seti = set(arr)
    if lcm(*arr) not in seti:
        print(n)
        return
    ans = 0
    maxi = max(arr)
    last = isqrt(maxi)
    i = 1
    while i <= last:
        temp = 1
        if maxi % i == 0:
            if i not in seti:
                temp = 1
                count = 0
                for j in range(n):
                    if i % arr[j] == 0:
                        temp = lcm(temp, arr[j])
                        count += 1
                if temp == i:
                    ans = max(ans, count)
            if maxi // i not in seti:
                temp = 1
                count = 0
                for j in range(n):
                    if (maxi // i) % arr[j] == 0:
                        temp = lcm(temp, arr[j])
                        count += 1
                if temp == maxi // i:
                    ans = max(ans, count)
                    
        i += 1
    
    print(ans)


for t in range(int(input())):
    solve()