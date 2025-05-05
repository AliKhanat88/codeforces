import sys
input = sys.stdin.readline
from collections import defaultdict

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])


    def update(self, index, val):
        i = index + len(self.tree) // 2  
        self.tree[i] += val
        while i > 1:
            i = i // 2
            self.tree[i] = max(self.tree[i * 2] , self.tree[i * 2 + 1] )
        
    def query(self, l, r):
        # [l, r)
        l = l + self.n
        r = r + self.n

        ans = -1
        while l < r:
            if l % 2 == 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                ans = max(ans, self.tree[r])
                
            l = l // 2
            r = r // 2
        return ans

def get_seg_index(x, i, n):
    return x - i + n -1

# def main()
def solve():
    n, k, q = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    # print(n, k, q)
    # print(arr)
    tree_n = 2 * (n)
    tree = SegTree([0] * (tree_n))
    ans = [0] * n
    dict = defaultdict(lambda:-1)
    for i in range(k):
        temp = get_seg_index(arr[i], i, n)
        tree.update(temp, 1)
        dict[i] = temp
    ans[0] = k - tree.query(0, tree_n)
    for i in range(k, n):
        tree.update(dict[i-k], -1)
        tree.update(get_seg_index(arr[i], i, n), 1)
        ans[i-k+1] = k - tree.query(0, tree_n)
        dict[i] = get_seg_index(arr[i], i, n)
    # print(ans)
    for i in range(q):
        l, r = map(int, input().split())
        print(ans[l-1])
for t in range(int(input())):
    solve()
# main()
    