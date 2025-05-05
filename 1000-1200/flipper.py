for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        if arr[0] == n:
            n -= 1
        if arr[-1] != n:
            ind = arr.index(n)
            for i in range(ind, len(arr)):
                print(arr[i], end = " ")
            print(arr[ind-1], end= " ")
            i = ind - 2
            while i >= 0 and arr[i] > arr[0]:
                print(arr[i], end=" ")
                i = i-1
            for i in range(i+1):
                print(arr[i], end= " ")
        elif arr[-1] == n and len(arr) == n:
            ind = arr.index(n)
            i = ind -1
            print(arr[ind], end= " ")
            while i >= 0 and arr[i] > arr[0]:
                print(arr[i], end=" ")
                i = i-1
            for i in range(i+1):
                print(arr[i], end=" ")
        elif arr[-1] == n and len(arr) != n:
            print(n, end=" ")
            for i in range(n):
                print(arr[i], end=" ")
        print()
