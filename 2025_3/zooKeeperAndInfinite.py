def solve():
    c, t = map(int, input().split())

    last = 31
    while last >= 0:
        if (c & (1 << last)) != (t & (1 << last)):
            if (c & (1 << last)):
                print("NO")
                return
            else:
                break
        last -= 1
    c_b = 0
    t_b = 0
    for b in range(last+1):
        if (c & (1 << b)):
            c_b += 1
        if (t & (1 << b)):
            t_b += 1
        if t_b > c_b:
            print("NO")
            return
    print("YES")
    

for t in range(int(input())):
    solve()