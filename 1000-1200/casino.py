def print_max_pot(n, m, data):
    data = list(zip(*data))
    count = 0
    for i in range(m):
        data[i] = sorted(data[i], reverse=True)
        sum = data[i][0]
        for j in range(1, n):
            count += sum - (data[i][j] * j)
            sum += data[i][j]
    print(count)

for t in range(int(input())):
    n, m = map(int, input().split())
    data = [0] * n
    for i in range(n):
        data[i] = list(map(int, input().split()))
    print_max_pot(n, m, data)