import sys
input = sys.stdin.readline
# from pprint import pprint
def solve():
    n, m = map(int, input().split())
    path = input().strip()
    data = [0] * n
    for i in range(n):
        data[i] = list(map(int, input().strip().split()))
    
    def sumRow(row):
        return sum(data[row])
    
    def sumCol(col):
        sumi = 0
        for i in range(n):
            sumi += data[i][col]
        return sumi

    # pprint(data)
    x = 10
    starti = 0
    startj = 0
    for i in range(len(path)):
        if path[i] == "D":
            data[starti][startj] = x - sumRow(starti)
            starti += 1
        else:
            data[starti][startj] = x - sumCol(startj)
            startj += 1
    
    data[starti][startj] = x - sumRow(n-1)
    for i in range(n):
        print(*data[i])
    assert sumCol(m-1) == sumRow(n-1)
    

    

for t in range(int(input())):
    solve()