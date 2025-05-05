def solve():
    a = input()
    b = input()
    i = len(b) -1
    j = len(a) -1
    can_do = False
    while i >= 0 and j >= 0:
        if b[i] == "1" and a[j] == "1":
            print(0)
            return
        if b[i] == "1":
            can_do = True
            per = j
            break
        i -= 1
        j -= 1
    j = per -1
    while j >= 0:
        if a[j] == "1":
            print(per - j)
            return
        j -= 1
    print(0)
for t in range(int(input())):
    solve()
        
