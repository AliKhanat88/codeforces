from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sumi_arr = [0] * (n + 1)

    for i in range(1, n):
        sumi_arr[i] = sumi_arr[i-1] + arr[i-1]
    dict = defaultdict(lambda:-1)
    dict[0] = 0
    per = 0
    ans = 0
    for i in range(n):
        if arr[i] == 0:
            ans += 1
            dict = defaultdict(lambda:-1)
            dict[0] = 0
            per = 0
        else:
            temp = per + arr[i]
            if dict[temp] != -1:
                ans += 1
                dict = defaultdict(lambda: - 1)
                dict[0] = 0
                per = 0
            else:
                dict[temp] = 0
                per = temp
            
    # print(sumi_arr)
    print(ans)
for t in range(int(input())):
    solve()