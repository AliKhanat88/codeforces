from collections import Counter
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    
    newarr = []
    per = arr[0]
    count = 1
    for i, num in enumerate(arr[1:]):
        if num != per:
            newarr.append((per, count))
            per = num
            count = 1
        else:
            count += 1
    
    newarr.append((per, count))
    MOD = 10 ** 9 + 7
    # print(newarr)
    def pro(a, b):
        return ((a % MOD) * (b % MOD)) % MOD
    def div(a, b):
        return ((a % MOD) * (pow(b, -1, MOD))) % MOD
    
    ans = 0
    cur = 1
    n = len(newarr)
    for i in range(min(m, n)):
        cur = pro(cur, newarr[i][1])
    if n >= m and newarr[m-1][0] - newarr[0][0] < m:
        ans += cur
    # print(ans, "pre")
    for i in range(m, n):
        cur = pro(cur, newarr[i][1])
        cur = div(cur, newarr[i-m][1])
        # print(cur, i)
        if newarr[i][0] - newarr[i-m+1][0] < m:
            ans = (ans + cur) % MOD
    print(ans)


    


for t in range(int(input())):
    solve()