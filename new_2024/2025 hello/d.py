INF = 2 ** 64
import sys
input = sys.stdin.readline
class MinSegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = min(self.tree[i * 2] , self.tree[i * 2 + 1])


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

        ans = INF
        while l < r:
            if l % 2 == 1:
                ans = min(ans , self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                ans = min(ans, self.tree[r])
                
            l = l // 2
            r = r // 2
        return ans


class MaxSegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = max(self.tree[i * 2] , self.tree[i * 2 + 1])


    def update(self, index, val):
        i = index + len(self.tree) // 2  
        self.tree[i] = val
        while i > 1:
            i = i // 2
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1]) 
        
    def query(self, l, r):
        # [l, r)
        l = l + self.n
        r = r + self.n

        ans = -INF
        while l < r:
            if l % 2 == 1:
                ans = max(ans , self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                ans = max(ans, self.tree[r])
                
            l = l // 2
            r = r // 2
        return ans

from heapq import heappop, heappush, heapify


def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    left = [0] * n
    right = [0] * n
    
    for i in range(n):
        left[i] = i + arr[i]
        right[i] = (n - i - 1) + arr[i]
    
    leftMin = MinSegTree(left)
    rightMin = MinSegTree(right)
    leftMax = MaxSegTree(left)
    rightMax = MaxSegTree(right)

    def find_max(index):
        org_val1 = left[index]
        org_val2 = right[index]
        maxi = max(org_val1 - leftMin.query(index, n), leftMax.query(0, index+1) - org_val1, org_val2 - rightMin.query(0, index+1), rightMax.query(index, n) - org_val2)
        return maxi
    
    heap = []
    for i in range(n):
        heap.append((-find_max(i), i))
    heapify(heap)
    print(-heap[0][0])

    for i in range(q):
        pi, num = map(int, input().split())
        pi -= 1
        arr[pi] = num
        leftMin.update(pi, num + pi)
        rightMin.update(pi, num + n - pi - 1)
        leftMax.update(pi, num + pi)
        rightMax.update(pi, num + n - pi - 1)
        left[pi] = num + pi
        right[pi] = num + n - pi - 1
        # print(leftMin.tree[n:])
        # print(rightMin.tree[n:])
        # print(find_max(pi))
        heappush(heap, (-find_max(pi), pi))
        while len(heap) > 0:
            if find_max(heap[0][1]) != -heap[0][0]:
                heappop(heap)
            else:
                break
        # print(arr)
        # print(heap[0])
        print(-heap[0][0])


for t in range(int(input())):
    solve()




        
    