import sys
input = sys.stdin.readline

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

    

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = max(arr)
    count = 1
    prr = list(map(int, input().split()))

    prr_index = [0] * n
    arr = [(arr[i], i) for i in range(n)]
    arr.sort()
    for i in range(n):
        prr_index[prr[i] - 1] = i

    # print(arr)
    # print(prr)
    # print(prr_index)
    seg = SegTree([1] * n)
    
    def find_max(x):
        l = 0
        r = n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            temp = seg.query(mid, n)
            if mid - temp >= -1:
                r = mid
            else:
                l = mid + 1
        temp = seg.query(l, n)
        if l - temp >= -1:
            return temp
        temp = seg.query(r, n)
        if r - temp >= -1:
            return temp
    for i in range(n):
        # print(i, arr[i])
        temp = find_max(arr[i][0])
        if maxi < arr[i][0] * temp:
            maxi = arr[i][0] * temp
            count = temp
        elif maxi == arr[i][0] * temp and count > temp:
            count = temp
        seg.update(prr_index[arr[i][1]], 0)
        # print(seg.tree[n:])
    print(maxi, count)


for t in range(int(input())):
    solve()