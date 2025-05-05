
 
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    a = [0] * (n+1)
    for num in arr:
        if num <= n:
            a[num] += 1
    # print(a)
    ans = [0] * (n+1)
    for i in range(1, n+1):
        if a[i] != 0:
            num = i
            while num <= n:
                ans[num] += a[i]
                num += i
    # print(ans)

    print(max(ans))
 
for t in range(int(input())):
    solve()



