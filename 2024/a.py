for t in range(int(input())):
    s = input()
    if len(s) <= 2:
        print("NO")
    elif len(s) == 3 and s[0] == "1" and s[1] == "0" and s[2] != "0" and s[2] != "1":
        print("YES")
    elif len(s) > 3 and s[0] == "1" and s[1] == "0" and s[2] != "0":
        print("YES")
    else:
        print("NO")