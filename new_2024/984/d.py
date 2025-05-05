import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().strip().split())
    data = [0] * n
    for i in range(n):
        data[i] = list(map(int, list(input().strip())))
    # print(data)
    ans = 0
    for i in range(min(n ,m) // 2):
        cur_b_r = n - i - 1
        cur_b_c = m - i - 1
        arr = []
        for j in range(i, cur_b_c + 1):
            arr.append(data[i][j])
        arr.pop()
        for j in range(i, cur_b_r + 1):
            arr.append(data[j][cur_b_c])
        arr.pop()
        for j in range(cur_b_c, i - 1, -1):
            arr.append(data[cur_b_r][j])
        arr.pop()
        for j in range(cur_b_r, i - 1, -1):
            arr.append(data[j][i])
        arr.pop()
        # print(arr)
        for i in range(len(arr)):
            if arr[i] == 1 and arr[(i+1) % len(arr)] == 5 and arr[(i+2) % len(arr)] == 4 and arr[(i+3) % len(arr)] == 3:
                ans += 1
    # arr = list(map(int, input().split()))
    print(ans)

for t in range(int(input())):
    solve()