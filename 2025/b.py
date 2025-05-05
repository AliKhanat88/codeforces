import sys
input = sys.stdin.readline

def solve():
    n, = map(int, input().split())
    arr = list(map(int, input().split()))
    if n % 2 == 1:
        print("NO")
        return
    c = [0] * (n+2)
    for num in arr:
        c[num] += 1
    # print(c)
    for i in range(1, n+1):
        if c[i] == 0:
            continue
        elif c[i] == 1:
            print("NO")
            return
        elif c[i] > 1:
            c[i+1] += c[i] - 2
    # print(c)
    if c[n+1] % 2 == 0:
        print("YES")
    else:
        print("NO")
        



for t in range(int(input())):
    solve()