for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if arr.count(1) % 2 == 0:
        mini = 0
    else:
        mini = 1
    if arr.count(1) <= n:
        print(mini, arr.count(1))
    else:
        print(mini, n - (arr.count(1) - n))