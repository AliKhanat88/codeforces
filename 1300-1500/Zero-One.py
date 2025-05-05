def solve():
    n, x, y = map(int, input().split())
    a = input()
    b = input()
    per = False
    done = False
    t = 0
    for i in range(n):
        if a[i] != b[i]:
            t += 1
            if per == True:
                done = True
            per = True
        else:
            per = False
    if t == 2 and done == True:
        print(min(x, y * 2))
    elif t % 2 == 1:
        print(-1)
    else:
        print(y * t // 2)

for t in range(int(input())):
    solve()
