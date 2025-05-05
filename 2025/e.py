import sys
input = sys.stdin.readline

def solve():
    n, = map(int, input().split())
    arr = list(map(int, input().split()))
    print(n, arr)


for t in range(int(input())):
    solve()