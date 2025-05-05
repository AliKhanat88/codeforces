import sys

input = sys.stdin.readline

def solve():
    a = 0
    b = 0
    n, m = map(int, input().strip().split())
    data = [[0] * n for j in range(m)]
    for i in range(n):
        j = 0
        for num in input().split():
            data[j][i] = int(num)
            j += 1
    if m == 1:
        print(1, 1)
        return
    for i in range(n):
        per = -1
        done = False
        first = False
        for j in range(1, m):
            if data[j][i] < data[j-1][i]:
                if first == False:
                    if per+1 != j-1:
                        data[per+1], data[j] = data[j], data[per+1]
                        a = per+1
                        b = j
                        done = True
                        break
                    else:
                        first = True
                else:
                    data[per+1], data[j] = data[j], data[per+1]
                    a = per+1
                    b = j
                    first = False
                    done = True
                    break
            elif data[j][i] > data[j-1][i] and first == False:
                per = j-1
        if done == True:
            break
        if first == True:
            data[per+1], data[per+2] = data[per+2], data[per+1]
            a = per+1
            b = per + 2
            break
    for i in range(n):
        for j in range(1, m):
            if data[j][i] < data[j-1][i]:
                print(-1)
                return
    print(a+1, b+1)

for t in range(int(input())):
    solve()