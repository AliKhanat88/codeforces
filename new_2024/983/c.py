from bisect import bisect_right

def solve():
    n = int(input())
    arr = list(map(int, input().split()))


    arr.sort()
    ans = 0
    c = []
    for i in range(1, n):
        c.append(arr[i] + arr[i-1])

    # print(c)
    mini = n
    for i in range(n-1, -1, -1):
        mini = min(mini, n - i - 1 + bisect_right(c, arr[i]))
    print(mini)

for t in range(int(input())):
    solve()