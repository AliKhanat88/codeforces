def solve():
    n, k = map(int, input().split())

    if n % 2 == 0:
        if (k // 2) % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if ((k+1) // 2) % 2 == 0:
            print("YES")
        else:
            print("NO")

for t in range(int(input())):
    solve()