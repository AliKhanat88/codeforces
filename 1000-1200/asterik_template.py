def is_astrik(a,b):
    if a[0] == b[0]:
        print("YES")
        print(f"{a[0]}*")
        return
    if a[-1] == b[-1]:
        print("YES")
        print(f"*{a[-1]}")
        return
    i = 0
    while i < len(a)-1:
        j = 0
        while j < len(b)-1:
            if a[i:i+2] == b[j:j+2]:
                print("YES")
                print(f"*{a[i:i+2]}*")
                return
            j += 1
        i += 1
    print("NO")

for t in range(int(input())):
    c = input()
    d = input()
    is_astrik(c,d)