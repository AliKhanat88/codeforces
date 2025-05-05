from collections import defaultdict
def solve():
    n, m = map(int, input().split())
    sumi = 0
    dict_row = defaultdict(lambda:[])
    dict_col = defaultdict(lambda:[])
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(m):
            dict_row[arr[j]].append(i)
            dict_col[arr[j]].append(j)
    for val in dict_row.values():
        val = sorted(val)
        for i in range(len(val)):
            sumi += i * val[i] + (len(val) - i - 1) * val[i] * (-1)

    for val in dict_col.values():
        val = sorted(val)
        for i in range(len(val)):
            sumi += i * val[i] + (len(val) - i - 1) * val[i] * (-1)
    print(sumi)
solve()