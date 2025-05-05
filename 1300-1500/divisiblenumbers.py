from math import lcm, ceil

def solve():
    a, b, c, d = map(int, input().split())
    if a * 2 <= c and b * 2 <= d:
        print(a*2, b*2)
        return
    if c-a > d-b:
        for i in range(b+1, d+1):
            temp = lcm(i, a*b) // i
            if ceil((a+1) / temp) * temp <= c:
                print(ceil((a+1) / temp) * temp, i)
                return 
    else:
        for i in range(a+1, c+1):
            temp = lcm(i, a*b) // i
            if ceil((b+1) / temp) * temp <= d:
                print(i, ceil((b+1) / temp) * temp)
                return 

    print(-1, -1)
            

            


for t in range(int(input())):
    solve()