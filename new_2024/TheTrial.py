import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    s = input().strip()
    data = [0] * n
    for i in range(n):
        data[i] = list(map(int, input().split()))
    def col_sum(col):
        sumi = 0
        for i in range(n):
            sumi += data[i][col]
        return sumi
    def row_sum(row):
        sumi = 0
        for i in range(m):
            sumi += data[row][i]
        return sumi
    start = [0, 0]
    for c in s:
        if c == "D":
            data[start[0]][start[1]] = 0 - row_sum(start[0])
            start[0] += 1
        else:
            data[start[0]][start[1]] = 0 - col_sum(start[1])
            start[1] += 1
    data[start[0]][start[1]] = 0 - col_sum(start[1])
    for i in range(n):
        print(*data[i])



for t in range(int(input())):
    solve()