def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = 0
    visited = [-1] * n
    for i in range(30, -1, -1):
        even = 0
        odd = 0
        ans_arr = [0] * (n+2)
        lastActive = 0
        buffer = 0
        if arr[0] & (2 ** i) != 0 and visited[0] == -1:
            active_st = [(True, 0)]
        elif arr[0] & (2 ** i) != 0 and visited[0] != -1:
            active_st = [(False, 0)]
        else:
            active_st = []
        isEven = True
        # print("arrbit", [arr[j] & (2 ** i) != 0 for j in range(n)])
        # print("arrbit new", [arr[j] & (2 ** i) != 0 and visited[j] == -1 for j in range(n)])
        for j in range(n):
            lastActive = 0
            for k in range(len(active_st)-1, max(-1, len(active_st)-3), -1):
                if active_st[k][0] == True:
                    lastActive += 1
            if len(active_st) >= 3:
                last_index = active_st[-3][1]
            else:
                last_index = 0
            if arr[j] & (2 ** i) != 0:
                even, odd = odd, even+buffer+1
                buffer = 0
                isEven = not isEven
                if visited[j] == -1:
                    visited[j] = 0
                    ans_arr[j+2] = ans_arr[last_index+2] + even * lastActive
                else:
                    ans_arr[j+2] = ans_arr[last_index+2] + even * lastActive
            else:
                buffer += 1
                ans_arr[j+2] = ans_arr[j+1]
            # print("even odd isEven ans 2 ** i", even, odd, ans_arr, 2 ** i, lastActive, active_st)
            if j+1 < n and arr[j+1] & (2 ** i) != 0 and visited[j+1] == -1:
                active_st.append((True, j+1))
            elif j+1 < n and arr[j+1] & (2 ** i) != 0 and visited[j+1] != -1:
                active_st.append((False, j +1))
        ans += sum(ans_arr)
    print(ans)
                
for t in range(int(input())):
    solve()