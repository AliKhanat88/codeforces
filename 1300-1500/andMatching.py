def solve():
    n, k = map(int, input().split())

    if n == 4 and k == 3:
        print(-1)
    else:
        if k == 0:
            for i in range(n//2):
                print(i, n-1-i)
        elif k < n-1:
            print(n-1, k)
            
            for i in range(1, n//2):
                if n-i-1 == k:
                    print(0, i)
                elif i == k:
                    print(0, n-i-1)
                else:
                    print(i, n-1-i)
        else:
            print(n-1,n-2)
            print(1, 3)
            print(n-4, 0)
            for i in range(1,n//2):
                if i == 1 or i == 3:
                    pass
                else:
                    print(i, n-1-i)

                

for t in range(int(input())):
    solve()