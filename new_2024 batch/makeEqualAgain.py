def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    equal_front = 1
    i = 1
    while i < n:
        if arr[i] == arr[0]:
            equal_front += 1
            i += 1
        else:
            break
    if i == n:
        print(0)
        return
    equal_back = 1
    j = n-2
    while j >= i:
        if arr[j] == arr[-1]:
            equal_back += 1
            j -= 1
        else:
            break
    if arr[0] == arr[-1]:
        print(n-equal_back -equal_front)
    else:
        print(n - max(equal_front, equal_back))
    

    


for t in range(int(input())):
    solve()