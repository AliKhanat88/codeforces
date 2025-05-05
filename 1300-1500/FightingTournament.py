inf = 1000000000

def solve():
    n, q = map(int, input().split())
    arr = list(map(int,input().split()))

    wins = [0] * n
    last_ind = 0
    for i in range(1, n):
        if arr[last_ind] > arr[i]:
            wins[last_ind] += 1
        else:
            last_ind = i
            wins[last_ind] += 1
    wins[last_ind] = inf
    # print(wins)
    for j in range(q):
        i, k = map(int, input().split())
        if i == 1 or i == 2:
            temp = 0
        else:
            temp = i - 2
        print(max(min(wins[i-1], k - (temp)), 0))

for t in range(int(input())):
    solve()