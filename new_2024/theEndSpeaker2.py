import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

MOD = 10 ** 9 + 7
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = (self.tree[i * 2] + self.tree[i * 2 + 1]) % MOD


    def update(self, index, val, keep=False):
        i = index + len(self.tree) // 2  
        if keep:
            self.tree[i] = (self.tree[i] + val) % MOD
        else:
            self.tree[i] = val % MOD
        while i > 1:
            i = i // 2
            self.tree[i] = (self.tree[i * 2] + self.tree[i * 2 + 1]) % MOD
        
    def query(self, l, r):
        # [l, r)
        l = l + self.n
        r = r + self.n

        ans = 0
        while l < r:
            if l % 2 == 1:
                ans += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                ans += self.tree[r]
                
            l = l // 2
            r = r // 2
            ans = ans % MOD
        return ans


inf = 99999999999999999999999
def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    sumi_arr = [0] * (n + 1)
    for i in range(1, n + 1):
        sumi_arr[i] = sumi_arr[i-1] + arr[i-1]
    mini_dp = [inf] * (n+1)


    mini_dp[0] = 0

    maxi_arr = [0] * n
    maxi = -1
    for i in range(n-1, -1, -1):
        maxi = max(maxi, arr[i])
        maxi_arr[i] = maxi
    seg = SegTree([0] * (n + 1)) 
    seg.update(0, 1)
    for i in range(m):
        j = 1
        while j < n + 1:
            if maxi_arr[j-1] > brr[i]:
                j += 1
                continue
            mini_index = bisect_left(sumi_arr, sumi_arr[j] - brr[i])
            # print(j, mini_index, brr[i])
            min_val = mini_dp[mini_index]
            left_min_ind = bisect_left(mini_dp, min_val)
            right_min_ind = bisect_right(mini_dp, min_val)
            left_min_ind = max(left_min_ind, mini_index)
            right_min_ind = min(right_min_ind, j)
            # print("Before")
            # print(i, j)
            # print("mini_val", min_val)
            # print(left_min_ind)
            # print(right_min_ind)
            # print(mini_dp)
            # print(seg.tree[n+1:])
            # print(mini_dp[j],  mini_dp[mini_index] + m - (i + 1))
            if mini_dp[j] == mini_dp[mini_index] + m - (i + 1):
                seg.update(j, seg.query(left_min_ind, right_min_ind), keep=True)
            elif mini_dp[j] > mini_dp[mini_index] + m - (i + 1):
                seg.update(j, seg.query(left_min_ind, right_min_ind), keep=False)
            mini_dp[j] = min(mini_dp[j], mini_dp[mini_index] + m - (i + 1))
            # print("After")
            # print(mini_dp)
            # print(seg.tree[n+1:])
            j += 1
    
    # print(mini_dp)

    if mini_dp[-1] >= inf:
        print(-1)
        return 
    else:
        print(mini_dp[-1], seg.query(n, n+1))
    


for t in range(int(input())):
    solve()