import sys
input = sys.stdin.readline

def solve():
    input()
    n, m = map(int, input().split())
    data = [[] for i in range(n)]
    max_second_max = -1
    index = None
    for i in range(n):
        data[i] = list(map(int, input().split()))
        first_max = max(data[i][0], data[i][1])
        second_max = min(data[i][0], data[i][1])
        for j in range(2, m):
            if data[i][j] > first_max:
                second_max = first_max 
                first_max = data[i][j]
            elif second_max < data[i][j]:
                second_max = data[i][j]
        if second_max > max_second_max:
            max_second_max = second_max
            index = i
    # print("TEST")
    # print(max_second_max)
    # print(index)
    if n >= m:
        first = data[index].index(max(data[index]))
        second = data[index].index(max_second_max)
    else:
        first = None
        second = None

    mini = max_second_max
    for i in range(m):
        if i != first and i != second:
            maxi = -1
            for j in range(n):
                maxi = max(maxi, data[j][i])
            mini = min(mini, maxi)
    print(mini)

for t in range(int(input())):
    solve()