for t in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n % 2 == 1:
        print(-1)
    else:
        for i in range(1, n+1, 2):
            print(i+1, i, end=" ")
        print()