def solve():
    s = list(input())
    for i in range(len(s)):
        if s[i] == "X":
            s[i] = "_"
        elif s[i] == "_":
            s[i] = "X"
    s = "".join(s)
    if len(s) == 1:
        if s[0] in ("_", "X", "0"):
            print(1)
        else:
            print(0)
        return
    if len(s) == 2:
        if s[-2:] in ("25", "50", "75"):
            print(1)
        elif s[-2:] in ("2_", "5_", "7_"):
            print(1)
        elif s[-2:] in ("_0"):
            print(1)
        elif s[-2:] in ("_5"):
            print(2)
        elif s[-2:] in ("2X", "5X", "7X"):
            print(1)
        elif s[-2:] in ("X5"):
            print(2)
        elif s[-2:] in ("X0"):
            print(1)
        elif s[-2:] in ("X_", "_X", "XX"):
            print(3)
        else:
            print(0)
        return

    slash = False
    mult = 1
    if s[-2:] in ("00", "25", "50", "75"):
        mult = 1
    elif s[-2:] in ("2_", "7_"):
        mult = 1
        slash = True
    elif s[-2:] in ("0_", "5_"):
        if s[0] == "_":
            mult = 0
        else:
            mult = 1
        slash = True
    elif s[-2:] in ("_0"):
        if s[0] == "_":
            mult = 1
        else:
            mult = 2
        slash = True
    elif s[-2:] in ("_5"):
        mult = 2
        slash = True
    elif s[-2:] in ("0X", "2X", "5X", "7X"):
        mult = 1
    elif s[-2:] in ("X0", "X5"):
        mult = 2
    elif s[-2:] in ("_X"):
        if s[0] == "_":
            mult = 3
        else:
            mult = 4
        slash = True
    elif s[-2:] in ("X_"):
        if s[0] == "_":
            mult = 2
        else:
            mult = 4
        slash = True
    elif s[-2:] in ("__"):
        if s[0] == "_":
            mult = 0
        else:
            mult = 1
        slash = True
    elif s[-2:] in ("XX"):
        mult = 4
    else:
        print(0)
        return
    if s[0] == "0":
        print(0)
        return
    elif s[0] == "_" and slash == False:
        mult = mult * 9
        slash = True
    elif s[0] == "X":
        mult = mult * 9
    for i in range(1, len(s)-2):
        if s[i] == "_" and slash == False:
            mult = mult * 10
            slash = True
        elif s[i] == "X":
            mult = mult * 10
    print(mult)

# for t in range(int(input())):   
solve()