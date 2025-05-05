from math import sqrt, ceil

def solve():
    n = int(input())
    if n == 1:
        print(2)
        print(0, 1)
        return
    ans = set()
    ans.add(0)
    for i in range(1, ceil(sqrt(n)) + 1):
        ans.add(n // (n // i))
        ans.add(n // i)
    print(len(ans))
    for num in sorted(list(ans)):
        print(num, end=" ")
    print()

for i in range(int(input())):
    solve()