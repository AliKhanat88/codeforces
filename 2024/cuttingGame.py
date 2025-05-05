

import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    con_row = []
    con_col = []
    a,b,n,m = map(int, input().split())
    dict = defaultdict(lambda: False)
    for i in range(n):
        c, d = map(int, input().split())
        con_row.append((c, d))
        con_col.append((c, d))
    con_row.sort(key = lambda x: x[0])
    con_col.sort(key = lambda x: x[1])
    r_sta = 0
    r_end = a + 1
    c_sta = 0
    c_end = b + 1
    alice = 0
    ans = [0, 0]
    r1 = 0 
    r2 = n - 1
    c1 = 0
    c2 = n - 1
    # print("TEST")
    for i in range(m):
        temp = input().strip().split()
        temp[1] = int(temp[1])
        # print(temp, r_sta, r_end, c_sta, c_end, size)
        # print(con_row.in_order(), con_col.in_order())
        if temp[0] == "U":
            r_sta += temp[1]
            while r1 <= r2:
                if con_row[r1][0] <= r_sta:
                    if dict[con_row[r1]] == False:
                        ans[alice] += 1
                        dict[con_row[r1]] = True
                    r1 += 1
                else:
                    break
        elif temp[0] == "D":
            r_end -= temp[1]
            while r1 <= r2:
                if con_row[r2][0] >= r_end:
                    if dict[con_row[r2]] == False:
                        ans[alice] += 1
                        dict[con_row[r2]] = True
                    r2 -= 1
                else:
                    break
        elif temp[0] == "L":
            c_sta +=temp[1]
            while c1 <= c2:
                if con_col[c1][1] <= c_sta:
                    if dict[con_col[c1]] == False:
                        ans[alice] += 1
                        dict[con_col[c1]] = True
                    c1 += 1
                else:
                    break
        elif temp[0] == "R":
            c_end -= temp[1]
            while c1 <= c2:
                # print(con_col, c2)
                if con_col[c2][1] >= c_end:
                    if dict[con_col[c2]] == False:
                        ans[alice] += 1
                        dict[con_col[c2]] = True
                    c2 -= 1
                else:
                    break
        # print(temp)
        # print(con_row.in_order(), con_col.in_order())
        alice = (alice + 1) % 2
    print(ans[0], ans[1])
for i in range(int(input())):
    solve()