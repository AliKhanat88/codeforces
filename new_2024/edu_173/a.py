from math import log

def solve():
    n = int(input())
    if n <= 3:
        print(1)
        return
    count = 0
    while n > 3:
        n = n // 4
        count += 1
    print(2 ** count)


for t in range(int(input())):
    solve()