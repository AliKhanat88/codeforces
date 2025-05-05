import sys
input = sys.stdin.readline
from bisect import bisect_right, bisect_left

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]


    def update(self, index, val):
        i = index + len(self.tree) // 2  
        self.tree[i] = val
        while i > 1:
            i = i // 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1] 
        
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
        return ans

MOD = 998244353
def prod(a, b):
    return (a * b) % MOD

def divi(a, b):
    return (a * pow(b, MOD - 2, MOD)) % MOD


def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    crr = [(arr[i], 1) for i in range(n)] + [(brr[i], -1) for i in range(n)]
    crr.sort()
    cur = 0
    ans = 1
    for i in range(len(crr) -1, -1, -1):
        if cur > 0 and crr[i][1] == -1:
            ans = prod(ans, crr[i][0])
        elif cur < 0 and crr[i][1] == 1:
            ans = prod(ans, crr[i][0])
        cur += crr[i][1]

    seg = SegTree([num[1] for num in crr])
    print(ans)
    for i in range(q):
        o, a = map(int, input().split())
        a -= 1
        numi = (arr[a], 1)
        index = bisect_left(crr, numi)
        count = seg.query(index+1, 2*n)
        if count < 0:
            ans = divi(ans, arr[a])
        next = (arr[a] +1, -2)
        next_index = bisect_left(crr, next)
        if crr[next_index-1][1] == -1:
            seg.update(next_index-1, 1)
            seg.update(index, -1)
        crr[next_index-1], crr[index] = crr[index], crr[next_index-1]
        crr[next_index-1] = (crr[next_index - 1][0] + 1, 1)
        print(crr)
        count = seg.query(index+1, 2*n)
        if count > 0 and crr[index][1] == -1:
            ans = prod(ans, crr[index][0])
        elif count < 0 and crr[index][1] == 1:
            ans = prod(ans, crr[index][0])
        count = seg.query(next_index, 2*n)
        if count > 0 and crr[next_index-1][1] == -1:
            ans = prod(ans, crr[next_index-1][0])
        elif count < 0 and crr[next_index-1][1] == 1:
            ans = prod(ans, crr[next_index-1][0])
        arr[a] += 1
        if o == 2:
            numi = (brr[a], -1)
            index = bisect_left(crr, numi)
            count = seg.query(index+1, 2*n)
            if count > 0:
                ans = divi(ans, brr[a])
            next = (brr[a] +1, -2)
            next_index = bisect_left(crr, next)
            if crr[next_index-1][1] == 1:
                seg.update(next_index-1, -1)
                seg.update(index, 1)
            crr[next_index-1], crr[index] = crr[index], crr[next_index-1]
            crr[next_index-1] = (crr[next_index - 1][0] + 1, -1)
            print(crr)
            count = seg.query(index+1, 2*n)
            if count > 0 and crr[index][1] == -1:
                ans = prod(ans, crr[index][0])
            elif count < 0 and crr[index][1] == 1:
                ans = prod(ans, crr[index][0])
            count = seg.query(next_index, 2*n)
            if count > 0 and crr[next_index-1][1] == -1:
                ans = prod(ans, crr[next_index-1][0])
            elif count < 0 and crr[next_index-1][1] == 1:
                ans = prod(ans, crr[next_index-1][0])
            brr[a] += 1
        print(ans)

            





    
for t in range(int(input())):
    solve()