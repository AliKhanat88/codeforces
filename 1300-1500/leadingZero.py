from collections import defaultdict

def solve():
    s = input()
    n = len(s)
    k = int(input())
    if k == 0:
        print(s)
        return
    dict = defaultdict(lambda: [0,0,0,0,0,0,0,0,0,0])
    for i in range(10):
        dict[n][i] = 9999999999

    for i in range(n-1,-1,-1):
        for j in range(10):
            if int(s[i]) == j:
                dict[i][j] = 0
            else:
                dict[i][j] = dict[i+1][j] + 1
    ans = []
    for i in range(1, 10):
        if dict[0][i] < k+1:
            k -= dict[0][i]
            start = dict[0][i] + 1
            ans.append(f"{i}")
            break
    while start < n:
        for j in range(10):
            if dict[start][j] < k+1:
                k -= dict[start][j]
                start = start + dict[start][j] + 1
                ans.append(f"{j}")
                break
    if k == 0:
        print("".join(ans))
    else:
        print("".join(ans[:-k]))

for i in range(int(input())):
    solve()