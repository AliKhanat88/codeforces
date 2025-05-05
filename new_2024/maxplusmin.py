import sys
input = sys.stdin.readline

class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (self.n * 2)
    

    def update(self, index, val):
        i = index + len(self.tree) // 2  
        self.tree[i] += val
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

    index_seg = {}

    for i, num in enumerate(sorted(arr)):
        index_seg[str(num)] = i

    def get_index(x):
        return index_seg[str(x)]
    
    left_even_seg = SegTree(n)
    left_odd_seg = SegTree(n)
    right_even_seg = SegTree(n)
    right_odd_seg = SegTree(n)

    for i in range(1, n):
        if i % 2 == 0:
            right_odd_seg.update(get_index(arr[i]), 1)
        else:
            right_even_seg.update(get_index(arr[i]), 1)
    
    per_add = -2
    per_rem = -1
    remove_next = 1
    for i in range(n):
        if per_add >= 0:
            if per_add % 2 == 0:
                left_odd_seg(get_index(arr[i]), 1)
            else:
                left_even_seg(get_index(arr[i]), 1)
        if per_rem >= 0:
            if per_rem % 2 == 0:
                left_odd_seg(get_index(arr[i]), 0)
            else:
                left_even_seg(get_index(arr[i]), 0)
        if remove_next < n:
            if remove_next % 2 == 0:
                right_odd_seg(get_index(arr[i]), 0)
            else:
                right_even_seg(get_index(arr[i]), 0)

        



for t in range(int(input())):
    solve()