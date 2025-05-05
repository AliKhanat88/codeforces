from bisect import bisect_left
import sys

input = sys.stdin.readline
def solve():
    n, q = map(int, input().split())
    check_row = [0] * (n+1)
    check_column = [0] * (n+1)
    arr_row = []
    arr_col = []
    for i in range(q):
        temp = input().strip().split()
        if temp[0] == "1":
            x, y = int(temp[1]), int(temp[2])
            if check_row[x] == 0:
                arr_row.insert(bisect_left(arr_row, x), x)
            if check_column[y] == 0:
                arr_col.insert(bisect_left(arr_col, y), y)
            check_row[x] += 1
            check_column[y] += 1
        elif temp[0] == "2":
            x, y = int(temp[1]), int(temp[2])
            check_row[x] -= 1
            check_column[y] -= 1
            if check_row[x] == 0:
                arr_row.pop(bisect_left(arr_row, x))
            if check_column[y] == 0:
                arr_col.pop(bisect_left(arr_col, y))
        else:
            x1, y1, x2, y2 = int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4])
            p1 = bisect_left(arr_row, x1)
            p2 = bisect_left(arr_row, x2)
            p3 = bisect_left(arr_col, y1)
            p4 = bisect_left(arr_col, y2)
            if p1 < len(arr_row) and p2 < len(arr_row) and arr_row[p1] == x1 and arr_row[p2] == x2 and abs(p2 - p1) == abs(x2 - x1):
                print("YES")
                
            elif p3 < len(arr_col) and p4 < len(arr_col) and arr_col[p3] == y1 and arr_col[p4] == y2 and abs(p4 - p3) == abs(y2 - y1):
                print("YES")
            else:
                print("NO")
        # print(arr_row)
        # print(arr_col)
solve() 