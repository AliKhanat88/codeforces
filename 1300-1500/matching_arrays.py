def solve():
    n,x = map(int, input().split())
    a = input().split()
    b = list(map(int, input().split()))
    a = [[i, int(a[i])] for i in range(n)]
    b.sort()
    a.sort(key=lambda x:x[1])
    k = n-1
    x = n - x
    for i in range(x-1,-1,-1):
        if a[i][1] > b[k]:
            print("NO")
            return 
        else:
            a[i][1] = b[k]
            k -= 1
    
    for i in range(n-1, x-1, -1):
        if a[i][1] <= b[k]:
            print("NO")
            return 
        else:
            a[i][1] = b[k]
            k -= 1
    print("YES")
    print_arr = [0] * n
    for i in range(n):
        print_arr[a[i][0]] = str(a[i][1])
    print(" ".join(print_arr))




for t in range(int(input())):
    solve()