def solve():
    a, b = map(int, input().split())

    if a % 2 == 1:
        print(b)
    else:
        if b % 2 == 0:
            print(b)
        else:
            print(b - 1)

# for t in range(int(input())):
solve()