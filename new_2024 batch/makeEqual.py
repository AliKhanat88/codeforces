def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    sumi = 0
    if sum(arr) % n != 0:
        print("NO")
        return

    equality = sum(arr) // n
    for i in range(n):
        if arr[i] < equality:
            if equality - arr[i] <= sumi:
                sumi -= (equality - arr[i])
            else:
                print("NO")
                return
        else:
            sumi += (arr[i] - equality)
    print("YES")




for t in range(int(input())):
    solve() 
    