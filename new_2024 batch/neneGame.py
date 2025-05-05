for t in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    qs = list(map(int, input().split()))

    for num in qs:
        print(min(num, arr[0]-1), end= " ")
    print()