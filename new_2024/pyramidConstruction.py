from copy import deepcopy
def solve(n):

    def check_bigger(arr, brr):
        arr = sorted(arr, key = lambda x: -x[0])
        brr = sorted(brr, key = lambda x: -x[0])
        if len(arr) > len(brr):
            return False
        if len(brr) > len(arr):
            return True
        for i in range(len(arr)):
            if arr[i][0] > brr[i][0]:
                return True
            elif brr[i][0] > arr[i][0]:
                return False
        return True

    dp = [None] * (n + 1)

    if n >= 5:
        dp[5] = [[5, 2, "H"]]
    if n >= 10:
        dp[10] = [[10, 3, "L"]]
    if n >= 20:
        dp[20] = [[20, 4, "L"]]

    for i in range(1, n + 1):
        if dp[i] != None:
            for j, num in enumerate(dp[i]):
                if num[2] == "H":
                    added = [num[0] + (num[1] + 1) ** 2, num[1] + 1, num[2]]
                if num[2] == "L":
                    added = [num[0] + (num[1] + 2) ** 2, num[1] + 2, num[2]]
                if added in dp[i]:
                    continue
                if num[2] == "H":
                    new_num = i + (num[1] + 1) ** 2
                    new_set = deepcopy(dp[i])
                    new_set[j][1] += 1
                    new_set[j][0] += (num[1] + 1) ** 2
                if num[2] == "L":
                    new_num = i + (num[1] + 2) ** 2
                    new_set = deepcopy(dp[i])
                    new_set[j][1] += 2
                    new_set[j][0] += (num[1] + 2) ** 2
                if new_num <= n:
                    if dp[new_num] == None:
                        dp[new_num] = new_set
                    else:
                        if check_bigger(new_set, dp[new_num]):
                            dp[new_num] = new_set
            new_num = i + 5
            if [5, 2, "H"] not in dp[i]:
                new_set = deepcopy(dp[i])
                new_set.append([5, 2, "H"])
                if new_num <= n:
                    if dp[new_num] == None:
                        dp[new_num] = new_set
                    else:
                        if check_bigger(new_set, dp[new_num]):
                            dp[new_num] = new_set
            new_num = i + 10
            if [10, 3, "L"] not in dp[i]:
                new_set = deepcopy(dp[i])
                new_set.append([10, 3, "L"])
                if new_num <= n:
                    if dp[new_num] == None:
                        dp[new_num] = new_set
                    else:
                        if check_bigger(new_set, dp[new_num]):
                            dp[new_num] = new_set
            new_num = i + 20
            if [20, 4, "L"] not in dp[i]:
                new_set = deepcopy(dp[i])
                new_set.append([20, 4, "L"])
                if new_num <= n:
                    if dp[new_num] == None:
                        dp[new_num] = new_set
                    else:
                        if check_bigger(new_set, dp[new_num]):
                            dp[new_num] = new_set

                
    print(dp)
    if dp[n] == None:
        print("impossible")
        return "impossible"
    print(*[f"{num[1]}{num[2]}" for num in sorted(dp[n], key= lambda x: -x[0])])
    return " ".join([f"{num[1]}{num[2]}" for num in sorted(dp[n], key= lambda x: -x[0])])



def brute(N):
    mx = 200
    l = [(i+1)**2 for i in range(mx)]

    ls = []

    h = 0
    sm = 0
    for i in  range(0,mx,2):
        sm += l[i]
        h += 1
        if sm > N: break
        if h > 1: ls.append((sm,i+1,'L'))

    h = 0
    sm = 0
    for i in  range(1,mx,2):
        sm += l[i]
        h += 1
        if sm > N: break
        if h > 1: ls.append((sm,i+1,'L'))

    h = 0
    sm = 0
    for i in  range(mx):
        sm += l[i]
        h += 1
        if sm > N: break
        if h > 1: ls.append((sm,h,'H'))

    ls.sort(key=lambda x: x[0],reverse=True)

    M = len(ls)


    INF = float('inf')
    dp = {}
    def foo(u,i):
        if u == 0:
            return 0
        if i == M or u < 0:
            return INF
        if (u,i) not in dp:
            dp[(u,i)] = min(foo(u,i+1),1 + foo(u-ls[i][0],i+1))
        return dp[(u,i)]


    ans = foo(N,0)

    if ans < INF:
        out = []
        u = N
        for i in range(M):
            if foo(u,i) == ans and foo(u-ls[i][0],i+1) == ans - 1:
                out.append(f'{ls[i][1]}{ls[i][2]}')
                ans -= 1
                u -= ls[i][0]
        print(' '.join(out))
        return ' '.join(out)
    else:
        print('impossible')
        return('impossible')





# n = int(input())
solve(44)

# for i in range(6, 100):
#     if solve(i) != brute(i):
#         print("Found")
#         print(i)
#         print(brute(i), "brute")
#         print(solve(i), "solve")
#         break
