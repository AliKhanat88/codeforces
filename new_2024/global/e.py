def solve():
    n, m = map(int, input().split())
    if m > 2 * n - 1:
        print("NO")
        return 
    print("YES")
    ans = []
    temp = []
    for i in range(n):
        temp.append(i + 1)
        temp.append(i + 1)
    for i in range(min(n, m)):
        ans.append(temp)
        temp = ans[-1][2:] + ans[-1][:2]

    temp = []
    for i in range(n):
        temp.append(i + 1)
        temp.append(i + 2)
    temp[-1] = 1
    for i in range(n, m):
        ans.append(temp)
        temp = ans[-1][2:] + ans[-1][:2]
    # print(ans)
    for i in range(2 * n):
        for j in range(m):
            print(ans[j][i], end=" ")
        print()
    
    


    

for t in range(int(input())):
    solve()