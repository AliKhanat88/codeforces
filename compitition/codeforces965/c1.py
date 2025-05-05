import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    points = [0] * n
    for i in range(n):
        points[i] = list(map(int, input().split()))

    x1, y1, x2, y2 = map(int, input().split())

    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    for i in range(n):
        temp = (x2 - points[i][0]) ** 2 + (y2 - points[i][1]) ** 2
        if temp <= d:
            print("NO")
            return
    print("YES")


for t in range(int(input())):
    solve()