from math import factorial
fact = [factorial(i) for i in range(9)]
def solve():
    n, d = map(int, input().split())
    for i in range(1, 10, 2):
        can = False
        for j in range(2, min(n + 1, 9)):
            if int(fact[j] * f"{d}") % i == 0:
                can = True
        if can:
            print(i, end= " ")
    print()
for t in range(int(input())):
    solve()