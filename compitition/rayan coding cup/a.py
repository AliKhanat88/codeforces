from math import lcm

def solve():
    a, b = map(int, input().split())
    print(lcm(a, b))


for t in range(int(input())):
    solve()