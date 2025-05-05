def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    sumi_arr = [0] * (n)
    mini_arr = [0] * (n)
    # print("TEST")
    # print(arr, k)
    cur_mini = 9999999999999999
    mini_index = None
    for i in range(n-1, -1, -1):
        if arr[i] < cur_mini:
            cur_mini = arr[i]
            mini_index = i
        mini_arr[i] = (cur_mini, mini_index)
    
    # print(mini_arr)

    remainder = k
    multiple = 99999999999999
    minus_term = 0
    i = 0 
    while i < n:
        multiple = min(remainder // (mini_arr[i][0] - minus_term), multiple)
        remainder = remainder - multiple * (mini_arr[i][0] - minus_term)
        sumi_arr[mini_arr[i][1]] = multiple 
        minus_term = mini_arr[i][0]
        i = mini_arr[i][1] + 1
        
        # print("remainder, multiple", remainder, multiple)

    # print(sumi_arr)
    ans = []
    cur_ans = 0
    for i in range(n-1, -1, -1):
        if sumi_arr[i] != 0:
            cur_ans = sumi_arr[i] - cur_ans + cur_ans
        ans.append(cur_ans)
    print(*reversed(ans))



for t in range(int(input())):
    solve()