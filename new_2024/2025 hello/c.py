def solve():
    l, r = map(int, input().split())
    b = 30
    ans = 0
    while b >= 0:
        if (2 ** b) & r != 0 and (2 ** b) & l == 0:
            break
        elif (2 ** b) & r != 0 and (2 ** b) & l != 0:
            ans += 2 ** b
        b -= 1
    # print("TEST")
    # print(l, r)
    # print(b)
    # print((2 ** b) ^ (2 ** b - 2), "print")
    ans += 2 ** b
    if ans -2 < l:
        print((ans), (ans - 1), (ans + 1))
    else:
        print((ans), (ans - 1), (ans - 2))
    



for t in range(int(input())):
    solve()