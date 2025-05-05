def print_max_operations(n, m, data):
    is_found = False
    count = 0
    for i in range(n):
        for j in range(m):
            if i != n-1:
                if data[i][j] == 0 and data[i+1][j] == 0:
                    is_found = True
            if j != m-1:
                if data[i][j] == 0 and data[i][j+1] == 0:
                    is_found = True
            if i != n-1 and j != m-1:
                if data[i+1][j+1] == 0 and data[i][j] == 0:
                    is_found = True
            if i != 0 and j != m-1:
                if data[i-1][j+1] == 0 and data[i][j] == 0:
                    is_found = True
            count += data[i][j]
    if is_found == True:
        print(count)
    else:
        if count == n * m:
            print(count - 2)
        else:
            print(count - 1)
            
for t in range(int(input())):
    n, m = map(int, input().split())
    data = [0] * n
    for i in range(n):
        data[i] = list(map(int, list(input())))
    print_max_operations(n, m, data)
