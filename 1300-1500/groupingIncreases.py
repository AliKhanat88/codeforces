def solve():
    n = int(input())
    arr = [*map(int, input().split())]

    a = 999999999
    b = 999999999
    ans = 0
    for i in range(n):
        if (arr[i] > a and arr[i] > b):
            if a >= b:
                b = arr[i]
            else:
                a = arr[i]
            ans += 1
        elif (arr[i] <= a and arr[i] <= b):
            if a >= b:
                b = arr[i]
            else:
                a = arr[i]
        else:
            if a >= b:
                a = arr[i]
            else:
                b = arr[i]
    print(ans)
for t in range(int(input())):
    solve()