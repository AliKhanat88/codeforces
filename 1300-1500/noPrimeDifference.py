def solve():
    n, m = map(int, input().split())
    if m % 2 == 0:
        per = 1
        for i in range(1, n+1):
            print(" ".join([str(num) for num in range(per, per + m)]))
            per = per + m

    elif n % 2 == 0:
        for i in range(1, n+1):
            per = i
            for j in range(i, m+i):
                print(per, end=" ")
                per += n
            print()
    else:
        get = True
        i = 1
        cur = 1
        while i <= n-1:
            if get == True:
                print(" ".join([str(num) for num in range(cur, cur + m)]))
                cur += m
                per = cur
                cur += 1
                print(" ".join([str(num) for num in range(cur, cur + m)]))
                cur += m
                get = False
            else:
                print(per, end= " ")
                print(" ".join([str(num) for num in range(cur, cur + m -1)]))
                cur += (m - 1)
                print(cur + m -1, end = " ")
                print(" ".join([str(num) for num in range(cur, cur + m -1)]))
                cur += m
                get = True
            i += 2
        if get:
            print(" ".join([str(num) for num in range(cur, cur + m)]))
        else:
            print(per, end= " ")
            print(" ".join([str(num) for num in range(cur, cur + m-1)]))
                

for i in range(int(input())):
    solve()
    print()