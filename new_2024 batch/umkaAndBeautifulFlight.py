def feboncci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        start1 = 1
        start2 = 1
        for i in range(2, n+1):
            start2, start1 = start1 + start2, start2
        return start2
    
feboDict = {}

for i in range(44+2):
    feboDict[i] = feboncci(i)

def febonci(n):
    return feboDict[n]
# print(febonci(1))
def recur(n, start_x, start_y, x, y,isHor=True):
    # print(n, start_x, start_y, isHor)
    while True:
        if n == 1:
            return True
        if isHor:
            if y > start_y + febonci(n) - 1:
                start_y = start_y + febonci(n)
                n = n - 1
                isHor = not isHor
            elif y <= start_y + febonci(n-1) - 1:
                n = n - 1
                isHor = not isHor
            else:
                return False
        else:
            if x > start_x + febonci(n) - 1:
                start_x = febonci(n) + start_x
                n = n - 1
                isHor = not isHor
            elif x <= start_x + febonci(n-1) - 1:
                n = n - 1
                isHor = not isHor
            else:
                return False
def solve():
    n, x, y = map(int, input().split())
    # print("TEST")
    # print(n, x, y)
    # # print("----------")
    if recur(n, 1, 1, x, y):
        print("YES")
    else:
        print("NO")
for t in range(int(input())):
    solve()