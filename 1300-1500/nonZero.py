def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    temp = 0
    for i in range(n):
        if arr[i] != 0:
            temp += 1
    if temp % 2 == 1:
        print(-1)
        return 
    ans = []
    per = None
    for i in range(n):
        if per is None and arr[i] == 0:
            ans.append((i+1, i+1))
        elif per is None:
            per = [arr[i], i]
        else:
            if arr[i] == 1:
                if per[0] == 1:
                    if (per[1] - i) % 2 == 0:
                        ans.append((per[1]+1, i-1))
                        ans.append((i, i+1))
                    else:
                        ans.append((per[1]+1, i+1))
                    per = None
                elif per[0] == -1:
                    ans.append((per[1]+1, i))
                    ans.append((i+1, i+1))
                    per = None
            elif arr[i] == -1:
                if per[0] == -1:
                    if (per[1] - i) % 2 == 0:
                        ans.append((per[1]+1, i-1))
                        ans.append((i, i+1))
                    else:
                        ans.append((per[1]+1, i+1))
                    per = None
                elif per[0] == 1:
                    ans.append((per[1]+1, i))
                    ans.append((i+1, i+1))
                    per = None
    # print(per)
    if per != None and arr[-1] == 0:
        ans.append((per[1] +1, n))
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
for t in range(int(input())):
    solve()