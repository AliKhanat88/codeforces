from collections import defaultdict
def solve():
    n, m = map(int,input().split())
    data = [0] * n
    for i in range(n):
        data[i] = list(input())
    last = 0
    colors = ["W", "B"]
    row = defaultdict(lambda:0)
    col = defaultdict(lambda:0)
    for i in range(n):
        for j in range(m):
            if data[i][j] == "U":
                data[i][j] = colors[last]

                last = (last + 1) % 2      
                data[i+1][j] = colors[last]
                row[i] += 1
                row[i+1] += 1
                col[j] += 2

    for j in range(m):
        for i in range(n):
            if data[i][j] == "L":
                data[i][j] = colors[last]

                last = (last + 1) % 2      
                data[i][j+1] = colors[last]
                row[i] += 2
                col[j] += 1
                col[j+1] += 1
    for key, val in row.items():
        if val % 2 == 1:
            print(-1)
            return
    for key, val in col.items():
        if val % 2 == 1:
            print(-1)
            return
    for i in range(n):
        print("".join(data[i]))
            


for t in range(int(input())):
    solve()