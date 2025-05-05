from math import log2

def solve():
    n, k = map(int, input().split())
    if n == 1:
        print(k)
        return 
    temp = 2 ** int(log2(k)) - 1
    print(temp,k-temp, end= " ")
    for i in range(2, n):
        print(0, end=" ")
    print()
for t in range(int(input())):
    solve()