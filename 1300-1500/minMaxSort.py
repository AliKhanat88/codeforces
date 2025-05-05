from collections import defaultdict

def solve():
    n = int(input())
    arr = [*map(int, input().split())]

    dict = defaultdict(lambda:0)
    for i in range(n):
        dict[arr[i]] = dict[arr[i] - 1] + 1

    # print(dict)

    mini = n // 2
    for i in range(1, n+1):
        mini = min(mini, max(n - i, i - dict[i]))
    print(mini)
for t in range(int(input())):
    solve()