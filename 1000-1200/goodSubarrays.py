for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    per = 0
    for i in range(n):
        per = min(per + 1, arr[i])
        count += per
    print(count)