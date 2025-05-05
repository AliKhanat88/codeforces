from math import ceil
def solve():
    n = int(input())
    s = input()
    c = s.count("*")
    c = ceil(c / 2)
    if c == 0:
        print(0)
        return
    for i in range(n):
        if s[i] == "*":
            c -= 1
            if c == 0:
                ind = i
                break
    
    ans = 0
    i = ind + 1
    ind_up = ind
    
    while i < n:
        if s[i] == "*":
            ans += (abs(i - ind_up) -1)
            ind_up += 1
        i += 1
    i = ind - 1
    
    while i > -1:
        if s[i] == "*":
            ans += (abs(i - ind) -1)
            ind -= 1
        i -= 1
    print(ans)

for t in range(int(input())):
    solve()