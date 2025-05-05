import sys
input = sys.stdin.readline

def solve():
    a= list(map(int, input().split()))
    for i in range(1, 6):
        if i not in a:
            print(i)
            return



solve()