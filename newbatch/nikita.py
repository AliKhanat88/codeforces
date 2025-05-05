for t in range(int(input())):
    n, m = map(int, input().split())
    if n >= m:
        if (n - m) % 2 == 0:
            print('YES')
        else:
            print("NO")
    else:
        print("NO")