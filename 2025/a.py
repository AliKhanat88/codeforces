import sys
input = sys.stdin.readline

def solve():
    x, y = map(int, input().split())
    if y == x+1:
        print("YES")
    elif x > y and (x - y + 1) % 9 == 0:
        print("YES")
    else:
        print("NO")
    


for t in range(int(input())):
    solve()