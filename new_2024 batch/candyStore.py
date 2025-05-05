import sys
input = sys.stdin.readline
from math import lcm

def solve():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    # print("Test")
    # print(a)
    # print(b)
    ans = 1
    per = b[0]
    last = 0
    for i in range(1, n):
        temp = lcm(per, b[i])
        if temp != per:
            j = i
            while j >= last:
                if a[j] % (temp // b[j]) != 0:
                    ans += 1
                    per = b[i]
                    last = i
                    break
                j -= 1
            
        else:
            if a[i] % (temp // b[i]) != 0:
                ans += 1
                per = b[i]
                last = i
        per = lcm(per, b[i])
    print(ans)

for t in range(int(input())):
    solve()