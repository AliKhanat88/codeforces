import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    matrix = [0] * n
    for i in range(n):
        matrix[i] = input()

    backward = [[0 for i in range(n)] for i in range(n)]
    forward = [[0 for i in range(n)] for i in range(n)]
    ans = 0
    for i in range(n):
        temp_sum = [0] * n
        for j in range(n):
            if j > 0:
                temp_forward = forward[i][j-1]
            else:
                temp_forward = 0
            if (backward[i][j] - temp_forward) % 2 == 0 and matrix[i][j] == "1" or (backward[i][j] - temp_forward) % 2 == 1 and matrix[i][j] == "0":
                temp_sum[j] = 1
                ans += 1
        sumi = 0
        for k in range(n):
            if temp_sum[k] == 1:
                sumi += 1
            if k + 1 < n and i + 1 < n:
                forward[i+1][k+1] = forward[i][k] + sumi
            if k - 1 >= 0 and i + 1 < n:
                backward[i+1][k-1] = backward[i][k] + sumi
        if i + 1 < n:
            backward[i+1][-1] = backward[i+1][-2]
    
    print(ans)







for t in range(int(input())):
    solve()