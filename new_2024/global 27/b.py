def solve():
    n = int(input())
    if n == 1 or n == 3:
        print(-1)
    elif n == 2:
        print(66)
    elif n == 4:
        print(3366)
    elif n % 2 == 0:
        print("33" + "3" * (n - 4) + "66")
    elif n % 2 == 1:
        print("3" * (n - 4) + "6366")

for t in range(int(input())):
    solve()



# print(33333366 % 66 == 0)