from collections import defaultdict
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dict = defaultdict(lambda:0)
    per = a[0]
    dict[a[0]] = 1
    count = 1
    for i in range(1, n):
        if a[i] == per:
            count += 1
        else:
            if dict[per] < count:
                dict[per] = count
            per = a[i]
            count = 1
    if dict[per] < count:
        dict[per] = count
    dict2 = defaultdict(lambda:0)
    dict2[b[0]] = 1
    per = b[0]
    count = 1
    for i in range(1, n):
        if b[i] == per:
            count += 1
        else:
            if dict2[per] < count:
                dict2[per] = count
            per = b[i]
            count = 1
    if dict2[per] < count:
        dict2[per] = count
    for i, val in dict2.items():
        dict[i] += val
    print(max(list(dict.values())))
for t in range(int(input())):
    solve()