import sys
input = sys.stdin.readline
from bisect import bisect_left

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    kevin = arr[0]
    arr.sort()
    sort_brr = []
    for i in range(m):
        if brr[i] > kevin:
            sort_brr.append(brr[i])
    sort_brr.sort()
    # print(sort_brr)
    # print(brr, "brr")
    for i in range(m):
        if brr[i] <= kevin:
            sort_brr.append(brr[i])
    
    # print(sort_brr)
    # print(arr)
    all_ans = []
    for temp_k in range(1, m+1):
        ans = 0
        start = m % temp_k
        for j in range(start, m, temp_k):
            # print(j, temp_k)
            if sort_brr[j] <= kevin:
                ans += 1
            else:
                temp = bisect_left(arr, sort_brr[j])
                # print(temp)
                ans += (n - temp) + 1
        all_ans.append(ans)
    print(*all_ans)



for t in range(int(input())):
    solve()