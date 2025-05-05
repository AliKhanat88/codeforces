def solve():
    n = int(input())
    a = list(map(int, input().split()))
    p = [0] * (n+1)

    # checking for ele
    if a[0] <= n:
        p[a[0]] += 1
    for i in range(1, n-1):
        if a[i] - a[i-1] <= n:
            p[a[i]-a[i-1]] += 1
    
    s = set()
    for i in range(1, n+1):
        if p[i] == 0:
            s.add(i)

    if len(s) == 1:
        print("YES")
        return
    elif len(s) > 2:
        print("NO")
        return
    # checking for the avaliability
    if a[0] > n or p[a[0]] > 1:
        if a[0] == sum(s):
            print("YES")
            return
    for i in range(1, n-1):
        if a[i] - a[i-1] > n or p[a[i] - a[i-1]] > 1:
            if a[i] - a[i-1] == sum(s):
                print("YES")
                return
    print("NO") 

    # print(s)
for t in range(int(input())):
    solve()

