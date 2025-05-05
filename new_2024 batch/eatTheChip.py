def solve():
    h, w, xa, ya, xb, yb = map(int, input().split())

    if xb - xa >= 1:
        if (xb - xa) % 2 == 1:
            if abs(ya - yb) == 0:
                print("Alice")
            elif yb > ya:
                if min(w, ya + ((xb - xa) // 2 + 1)) >= min(w, yb + ((xb - xa) // 2)):
                    print("Alice")
                else:
                    print("Draw")
            elif ya > yb:
                # print(max(1, ya - ((xb - xa) // 2 + 1)) ,max(1, yb - ((xb - xa) // 2)))
                if max(1, ya - ((xb - xa) // 2 + 1)) <= max(1, yb - ((xb - xa) // 2)):
                    print("Alice")
                else:
                    print("Draw")
        elif (xb - xa) % 2 == 0:
            if abs(ya - yb) == 0:
                print("Bob")
            elif ya > yb:
                if min(w, ya + ((xb - xa) // 2)) <= min(w, yb + ((xb - xa) // 2)):
                    print("Bob")
                else:
                    print("Draw")
            elif ya < yb:
                if max(1, ya - ((xb - xa) // 2)) >= max(1, yb - ((xb - xa) // 2)):
                    print("Bob")
                else:
                    print("Draw")
        else:
            print("Draw")
    else:
        print("Draw")
        

for t in range(int(input())):
    solve()