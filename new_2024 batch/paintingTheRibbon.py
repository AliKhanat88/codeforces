for t in range(int(input())):
    n,m,k = map(int, input().split())
    temp = n // m
    if n % m != 0:
        temp += 1
    if n - temp <= k :
        print("NO")
    else:
        print("YES")