def solve():
    n, m , k = map(int, input().split())

    if m + n - 2 > k:
        print("NO")
        return
    if (k - (m + n - 2)) % 4 in (1, 3):
        print("NO")
        return
    print("YES")
    # rows
    for i in range(n-1):
        for j in range(m-1):
            print("B", end=" ")
        print()
    if (n-1) % 2 == 0:
        for i in range(m-1):
            if i % 2 == 0:
                print("R", end= " ")
            else:
                print("B", end= " ")
    else:
        for i in range(m-1):
            if i % 2 == 0:
                print("B", end= " ")
            else:
                print("R", end= " ")
    print()
    for i in range(n-1):
        if i % 2 == 0:
            print("R " * m)
        else:
            print("B " * m)
        


for t in range(int(input())):
    solve()