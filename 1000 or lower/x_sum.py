def maxi_x(n, m , board):
    arr_decreasing = []
    for i in range(m):
        sum = 0
        for j in range(i, -1, -1):
            sum += board[j-i][j]
        arr_decreasing.append(sum)

    for i in range(1, n):
        sum = 0
        for j in range(m -1, -1, -1):
            sum += board[i + j][j]
        arr_decreasing.append(sum)
    
    arr_increasing = []
    for i in range(n -1, 0, -1):
        sum = 0
        for j in range(i, n):
            sum += board[j][j]
        arr_increasing.append(sum)
    
    for i in range(m):
        sum = 0
        temp = 0
        for j in range(i, m):
            sum += board[temp][j]
            temp += 1
        arr_increasing.append(sum)

    row = 0
    col = n - 1
    maxi = -1
    for i in range(n):
        for j in range(m):
            temp = arr_decreasing[row + j] + arr_increasing[col + j] - board[i][j]
            if temp > maxi:
                maxi = temp
        row += 1
        col -= 1
    print(maxi)


def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        board = []
        for i in range(n):
            row = list(map(int, input().split()))
            board.append(row)
        maxi_x(n, m , board)
main()