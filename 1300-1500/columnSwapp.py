import sys
input = sys.stdin.readline
from bisect import bisect_left

def check_data(n, m, data):
    for i in range(n):
        for j in range(1, m):
            if data[i][j] < data[i][j-1]:
                return False
    return True

def solve():
    n, m = map(int, input().split())
    data = [[0 for i in range(m)] for i in range(n)]

    for i in range(n):
        arr = [*map(int, input().split())]
        data[i] = arr

    # print(data)

    for i in range(n):
        for j in range(1, m):
            if data[i][j] < data[i][j-1]:
                temp_arr = sorted(data[i])
                # print(temp_arr)
                indexs = []
                for k in range(m):
                    if temp_arr[k] != data[i][k]:
                        indexs.append(k)
                        if len(indexs) == 2:
                            break
                j, temp = indexs
                # print(j-1, temp)
                for i in range(n):
                    data[i][temp], data[i][j] = data[i][j], data[i][temp]
                if check_data(n, m, data) == True:
                    print(j+1, temp+1)
                else:
                    print(-1)
                return
    print(1, 1)
for t in range(int(input())):
    solve()