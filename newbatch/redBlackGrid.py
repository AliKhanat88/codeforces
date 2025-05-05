def pprint(mat):
    for i in range(len(mat)):
        print(*mat[i])

def solve():
    n, k = map(int, input().split())

    inc = (n-1) * 2 
    total = inc * n
    if k == 1 or k == total - 1:
        print("Impossible")
        return
    print("Possible")
    print(inc, total)

    start = True
    temp_k = k
    ans = []
    i = 0
    while i < n:
        if temp_k <= 0:
            break
        temp = [start] * n
        for j in range(1, n, 2):
            temp[j] = not temp[j]
        ans.append(temp)
        temp_k -= inc
        i += 1
    target = i - 1
    for i in range(target+1, n):
        new_app = [False] * n
        ans.append(new_app)
    
    if k % inc == 0:
        pprint(ans)
        return
    j = n - 1
    cur = (target + 1) * inc
    while cur > k:

        if cur == k:
            break
        elif cur - 3 >= k:
            ans[target][j] = False
            ans[target][j-1] = False
            j -= 2
        elif cur - k == 2:
            ans[target][j] = not ans[target][j]
            cur -= 2
        elif cur - k == 1:
            ans[target][j]



    pprint(ans)
    
for t in range(int(input())):
    solve()