import time
start = time.time()

def solve():
    n, x = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            temp = min((n - i * j) // (i + j), x - (i + j))
            # print(j)
            if temp <= 0:
                break
            ans += temp
    print(ans)


for t in range(int(input())):
    solve()

print(time.time() - start)