def print_move(n, m, board):
    if board[0][0] == "1":
        print(-1)
    else:
        operations = []
        for i in range(n-1, 0, -1):
            for j in range(m):
                if board[i][j] == "1":
                    operations.append(f"{i} {j+1} {i+1} {j+1}")
        for i in range(m-1, 0, -1):
            if board[0][i] == "1":
                operations.append(f"{1} {i} {1} {i+1}")
        print(len(operations))
        for op in operations:
            print(op)

for t in range(int(input())):
    n, m = map(int, input().split())
    board = [0] * n
    for i in range(n):
        board[i] = input()
    print_move(n, m, board)