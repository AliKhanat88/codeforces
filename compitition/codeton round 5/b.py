def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    temp = 0
    can_a = True
    can_b = True
    can_c = True
    for i in range(n):
        if (a[i] | x) == x and can_a:
            temp = temp | a[i]
        else:
            can_a = False
        if (b[i] | x) == x and can_b:
            temp = temp | b[i]
        else:
            can_b = False
        if (c[i] | x) == x and can_c:
            temp = temp | c[i]
        else:
            can_c = False
    if temp == x:
        print("YES")
    else:
        print("NO")

for t in range(int(input())):
    solve()