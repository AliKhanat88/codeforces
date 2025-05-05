def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0] * n
    used = set()
    for i in range(n-1, 0, -1):
        done = [-1] * n
        for j in range(len(arr)):
            if j in used:
                continue
            if done[arr[j] % i] != -1:
                ans[i] = (done[arr[j] % i] + 1, j + 1)
                used.add(j)
                break
            done[arr[j] % i] = j
    # print(ans)
    print("YES")
    for i in range(1, n):
        print(*ans[i])
        

for t in range(int(input())):
    solve()