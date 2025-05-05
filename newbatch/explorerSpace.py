import sys
input = sys.stdin.readline

from collections import defaultdict

from pprint import pprint

def solve():
    n, m, k = map(int, input().split())
    def get_moves(i, j):
        return [(i+1, j +0, "V"), (i + 0, j + 1, "H"), (i + 0, j-1, "H"), (i-1,j+ 0, "V")]

    inf = 999999999999999
    def valid_move(i, j):
        if i < n and i >= 0 and j < m and j >= 0:
            return True
        return False
    

    hor_dat = [0] * (n)
    for i in range(n):
        hor_dat[i] = list(map(int, input().split()))

    ver_dat = [0] * (n-1)
    for i in range(n-1):
        ver_dat[i] = list(map(int, input().split()))
    
    if k % 2 == 1:
        for i in range(n):
            print(*[-1 for i in range(m)])
        return
    
    def get_weight(node1,node2,dir):
        if dir == "H":
            return hor_dat[node1[0]][min(node1[1], node2[1])]
        else:
            return ver_dat[min(node1[0], node2[0])][node1[1]]

    actual_k = k // 2
    dp = [[[inf if i != 0 else 0 for i in range(actual_k + 1)] for i in range(m)] for j in range(n)]

    # print(dp)
    for step in range(1, actual_k+1):
        for i in range(n):
            for j in range(m):
                # print(i,j, step)
                moves = get_moves(i, j)
                for move in moves:
                    if valid_move(move[0], move[1]):
                        dp[i][j][step] = min(dp[i][j][step], dp[move[0]][move[1]][step-1] + get_weight((i, j), (move[0], move[1]), move[2]))
    
    # print(dp)
    for i in range(n):
        print(*[dp[i][j][actual_k] * 2 for j in range(m)])



    




solve()