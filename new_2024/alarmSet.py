def solve():
    n = int(input())
    arr = [0] * 1000
    for i in range(n):
        h, m = map(int, input().split(":"))
        if h == 7:
            temp = 7 * 100 + 40 + m
        elif h == 8:
            temp = 8 * 100 + m
        else:
            temp = 860
        arr[temp] = 1
    cur = 0
    mini = 3
    for i in range(740, 861):
        cur += arr[i]
        cur -= arr[i - 11]
        mini = min (mini, max(0, 3 - cur))
    print(mini)



# for t in range(int(input())):
solve()