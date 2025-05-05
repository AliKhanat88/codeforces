def solve():
    n , x = map(int, input().split())
    arr = list(map(int, input().split()))

    sumi_arr = [0] * (n+1)
    cur_maxi = 0
    per = 0
    for k in range(n):
        cur_maxi += arr[k] + x
        if cur_maxi < 0: 
            cur_maxi = 0
            per = k + 1
        
        temp_maxi = cur_maxi
        sumi = 0
        for i in range(per, k+1):
            sumi_arr[k-i+1] = max(sumi_arr[k-i+1], temp_maxi)
            temp_maxi -= x
            sumi += arr[i]
            if sumi < 0:
                temp_maxi -= sumi
                sumi = 0
        sumi_arr[0] = max(sumi_arr[0], temp_maxi)
    per = arr[0]    
    for i in range(n+1):
        if sumi_arr[i] > per:
            per = sumi_arr[i]
        print(per, end=" ")
    print()
for t in range(int(input())):
    solve()