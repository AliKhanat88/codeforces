def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    posi_max = 0
    negi_max = 0
    posi_max_pos = 0
    negi_max_pos = 0
    for i, num in enumerate(arr):
        if num < 0:
            if abs(num) > negi_max:
                negi_max = abs(num)
                negi_max_pos = i + 1
        else:
            if num > posi_max: 
                posi_max = num
                posi_max_pos = i + 1
    if negi_max == 0 and posi_max == 0:
        print(0)
    elif posi_max >= negi_max:
        print(n * 2)
        print(1, posi_max_pos)
        print(1, posi_max_pos)
        for i in range(2, n+1):
            print(i, i-1)
            print(i, i-1)
    else:
        print(n * 2)
        print(n, negi_max_pos)
        print(n, negi_max_pos)
        for i in range(n-1, 0, -1):
            print(i, i+1)
            print(i, i+1)
    

for t in range(int(input())):
    solve()