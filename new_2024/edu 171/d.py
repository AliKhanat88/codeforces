def find_index(x, n):
    l = 1 
    r = n
    while l + 1 < r:
        mid = (l + r) // 2
        if ((mid + n) * (n - mid + 1)) // 2 <= x:
            l = mid
        else:
            r = mid - 1
    if ((l + n) * (n - l + 1)) // 2 <= x:
        return l
    else:
        return r

def give_total(mid, n):
    return ((mid + n) * (n - mid + 1)) // 2

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    multi = [0] * (n)
    for i in range(n):
        multi[i] = (n - i) * arr[i]

    sumi_arr = [0] * (n + 1)
    temp_sum = sum(multi)
    per = 0
    for i in range(1, n+1):
        temp_sum = temp_sum - per
        sumi_arr[i] = temp_sum
        per += multi[i-1]
    
    print(sumi_arr)

    total_sum = [0] *(n+1)
    for i in range(1, n+1):
        total_sum[i] = total_sum[i-1] + sumi_arr[i]
    

    q = int(input())
    for i in range(q):

        l, r= map(int, input().split())
        ans = 0
        offset_l = 0
        offset_r = 0
        index_l = find_index(l, n)
        if give_total(index_l - 1, n) != l:
            index_l += 1
            offset_l = l - give_total(index_l, n)
        index_r = find_index(l, n)
        if give_total(index_r, n) != l:
            index_r -= 1
            offset_r = give_total(index_r + 1, n) - r
        ans = total_sum[index_r] - total_sum[index_l]
        ans += 
        
        


for t in range(int(input())):
    solve()