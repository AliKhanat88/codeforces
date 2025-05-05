def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    # print(arr)
    i = 0
    while i < n:
        if arr[i] < arr[i-1]:
            break
        i += 1
    # print(i)
    arr = arr[i:] + arr[:i]
    # print(arr)
    j = 1
    while j < n:
        if arr[j] < arr[j-1]:
            print("NO")
            return
        j += 1
    print("YES")
    
    
for t in range(int(input())):
    solve()