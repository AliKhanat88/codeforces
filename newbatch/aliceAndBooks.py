for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr[-1] + max(arr[:-1]))