from math import gcd
def solve():
    l, r, g = map(int, input().split())
    if l % g == 0:
        per = l // g
    else:
        per = (l // g) + 1
    last = r // g
    maxi = -1
    ans = (-1, -1)
    for i in range(100):
        temp_last = last
        for j in range(100):
            if gcd(per+i, temp_last) != 1:
                temp_last -= 1
                continue
            else:
                if maxi < temp_last * g - (per + i) * g:
                    maxi = temp_last * g - (per + i) * g
                    ans = ((per+i) * g, temp_last * g)
                break
    if ans[0] >= l and ans[0] <= r and ans[1] >= l and ans[1] <= r:
        print(ans[0], ans[1])
    else:
        print(-1, -1)

    
        

for t in range(int(input())):
    solve()