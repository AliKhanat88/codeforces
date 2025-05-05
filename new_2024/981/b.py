def solve():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        temp_i = i
        temp_j = 0
        mini = 0
        while temp_i < n and temp_j < n:
            mini = min(mini, data[temp_i][temp_j])
            temp_i += 1
            temp_j += 1
        if mini < 0:
            ans += abs(mini)
    for i in range(1, n):
        temp_i = 0
        temp_j = i
        mini = 0
        while temp_i < n and temp_j < n:
            mini = min(mini, data[temp_i][temp_j])
            temp_i += 1
            temp_j += 1
        if mini < 0:
            ans += abs(mini)
    print(ans)
for t in range(int(input())):
    solve()