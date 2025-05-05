import sys
input = sys.stdin.readline
def solve():
    b, n = map(int, input().split())
    mod = b
    done = set()
    for k in range(n):
        temp = mod % n
        if temp in done:
            print(0)
            return
        done.add(temp)
        if temp == 0:
            print(1, k+ 1)
            return
        elif temp == 1:
            print(2, k + 1)
            return
        elif temp == n - 1:
            print(3, k + 1)
            return
        mod = temp * b
    
for t in range(int(input())):
    solve()