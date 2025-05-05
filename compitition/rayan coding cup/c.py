def is_valid(i, j, n, m):
    if i >= 0 and  i <= n-1 and j >= 0 and j <= m-1:
        return True
    return False

def solve():
    n, m = map(int, input().split())
    arr = [0] * n
    for i in range(n):
        arr[i] = list(input().strip())
    if n == 1 and m == 1:
        print(0)
        return
    done = [[False for i in range(m)] for i in range(n)]
    stack = []
    dict = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }
    for i in range(m):
        if arr[0][i] == "U":
            stack.append((0, i))
            done[0][i] = True
        if arr[n-1][i] == "D":
            stack.append((n-1, i))
            done[n-1][i] = True
    for i in range(n):
        if arr[i][0] == "L":
            stack.append((i, 0))
            done[i][0] = True
        if arr[i][m-1] == "R":
            stack.append((i, m-1))
            done[i][m-1] = True
    moves = [(-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)]
    while len(stack) != 0:
        cur = stack.pop()
        for move in moves:
            new_i = cur[0] + move[0]
            new_j = cur[1] + move[1]
            if is_valid(new_i, new_j, n, m) and done[new_i][new_j] == False and arr[new_i][new_j] != "?":
                oper = dict[arr[new_i][new_j]]
                temp_i, temp_j = oper[0] + new_i, oper[1] + new_j
                if temp_i == cur[0] and temp_j == cur[1]:
                    stack.append((new_i, new_j))
                    done[new_i][new_j] = True

    count = 0
    for i in range(n):
        for j in range(m):
            if done[i][j] == True:
                count += 1
            else:
                if arr[i][j] == "?":
                    can = True
                    for move in moves:
                        new_i = i + move[0]
                        new_j = j + move[1]
                        if is_valid(new_i, new_j, n, m) and done[new_i][new_j] != True:
                            can = False
                            break
                    if can == True:
                        count += 1
                    
    print(n * m - count)

    
        

    

for t in range(int(input())):
    solve()