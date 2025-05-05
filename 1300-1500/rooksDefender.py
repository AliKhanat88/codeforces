from collections import Counter
import sys
input = sys.stdin.readline

def update(i, n, arr, v):
    while i <= n:
        arr[i] += v
        i += i & (-i)

def query(i, n, arr):
    s = 0
    while i > 0:
        s += arr[i]
        i -= i & (-i)
    return s
def solve():
    n, q = map(int, input().split())
    cr = Counter()
    cc = Counter()
    check_row = [0] * (n+1)
    check_column = [0] * (n+1)
    for i in range(q):
        temp = [*map(int, input().strip().split())]
        if temp[0] == 1:
            _, x, y = temp
            cr[x] += 1
            cc[y] += 1
            if cr[x] == 1: update(x, n, check_row, 1)
            if cc[y] == 1: update(y, n, check_column, 1)
        elif temp[0] == 2:
            _, x, y = temp
            cr[x] -= 1
            cc[y] -= 1
            if cr[x] == 0: update(x, n, check_row, -1)
            if cc[y] == 0: update(y, n, check_column, -1)
        else:
            _, x1, y1, x2, y2 = temp
            if x2 - x1 + 1 <= query(x2, n, check_row) - query(x1-1, n, check_row):
                print("YES")
            elif y2 - y1 + 1 <= query(y2, n, check_column) - query(y1-1, n, check_column):
                print("YES")
            else:
                print("NO")
        # print(arr_row)
        # print(arr_col)
solve() 