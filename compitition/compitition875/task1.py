for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for num in arr:
        print(n - num + 1, end = " ")
    print()