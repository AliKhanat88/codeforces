import sys
input = sys.stdin.readline
def print_mini(n, m, d, p, a):
    dict = {}
    for i in range(n):
        dict[p[i]] = i+1
    mini = 9999999999999999999
    if d < n-1:
        for i in range(m-1):
            if dict[a[i+1]] < dict[a[i]] or dict[a[i+1]] > dict[a[i]] + d:
                print(0)
                return
            else:
                diff = dict[a[i+1]] - dict[a[i]]
                mini = min(mini, diff, d - diff + 1)
    else:
        for i in range(m-1):
            if dict[a[i+1]] < dict[a[i]] or dict[a[i+1]] > dict[a[i]] + d:
                print(0)
                return
            else:
                diff = dict[a[i+1]] - dict[a[i]]
                mini = min(mini, diff)
    print(mini)
for t in range(int(input())):
    n, m, d = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print_mini(n, m, d, p, a)