import sys
input = sys.stdin.readline

inf = 99999999999999999999999999
MOD = 998244353
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])


    def update(self, index, val):
        i = index + len(self.tree) // 2  
        self.tree[i] = val
        while i > 1:
            i = i // 2
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])
        
    def query(self, l, r):
        # [l, r)
        l = l + self.n
        r = r + self.n

        ans = inf
        while l < r:
            if l % 2 == 1:
                ans = min(ans, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                ans = min(ans, self.tree[r])
                
            l = l // 2
            r = r // 2
        return ans


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    seg = SegTree(arr)

    dp = [0] * (n + 2)
    # print(seg.tree[n:])
    # print(seg.query(2, 3))
    
    def find_index(x):
        l = x
        r = n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if seg.query(x, mid+1) != arr[x]:
                r = mid - 1
            else:
                l = mid
        # print(l, r)
        if seg.query(x, r+1) == arr[x]:
            return r
        else:
            return l
    # print(find_index(3))
    # print(seg.query(3, 5))
    sumi = [0] * (n + 2)
    dp[n] = 1
    sumi[n] = 1
    for i in range(n-1, -1, -1):
        temp = find_index(i)
        # print(arr[i], temp)
        dp[i] = (sumi[i+1] - sumi[temp+2]) % MOD
        sumi[i] = (sumi[i+1] + dp[i]) % MOD
    
    # print(dp)
    mini = arr[0]
    ans = dp[0]
    for i in range(1, n):
        if arr[i] < mini:
            ans += dp[i] % MOD
            mini = arr[i]
    print(ans % MOD)

for t in range(int(input())):
    solve()