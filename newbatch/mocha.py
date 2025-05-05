def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    
    arr.sort()

    first = arr[0]
    second = None
    for i in range(1, n):
        if arr[i] % first != 0:
            second = arr[i]
            break
    
    if second == None:
        second = first

    for i in range(n):
        if arr[i] % first != 0 and arr[i] % second != 0:
            print("NO")
            return
    print("YES")


for t in range(int(input())):
    solve()