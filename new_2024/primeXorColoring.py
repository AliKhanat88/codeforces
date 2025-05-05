def solve():
    n = int(input())
    if n == 1:
        print(1)
        print(1)
    elif n == 2:
        print(2)
        print(1, 2)
    elif n == 3:
        print(2)
        print(1, 2, 2)
    elif n == 4:
        print(3)
        print(1, 2, 2, 3)
    elif n == 5:
        print(3)
        print(1, 2, 2, 3, 3)
    else:
        cur = 0
        print(4)
        for i in range(n):
            print(cur + 1, end=" ")
            cur = (cur + 1) % 4
        print()

for t in range(int(input())):
    solve()