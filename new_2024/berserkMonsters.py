import sys
input = sys.stdin.readline

inf = 99999999999999999999999

class MinTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = i
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])


    def update(self, index, val):
        i = index + len(self.tree) // 2  
        self.tree[i] = val
        while i > 1:
            i = i // 2
            self.tree[i] = min(self.tree[i * 2] , self.tree[i * 2 + 1])
        
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


class MaxTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = i
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])


    def update(self, index, val):
        i = index + len(self.tree) // 2  
        self.tree[i] = val
        while i > 1:
            i = i // 2
            self.tree[i] = max(self.tree[i * 2] , self.tree[i * 2 + 1])
        
    def query(self, l, r):
        # [l, r)
        l = l + self.n
        r = r + self.n

        ans = -inf
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
    
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    drr = list(map(int, input().split()))
    if n == 1:
        print(0)
        return

    new_attack = [0] * n
    stack = []
    for i in range(1, n -1):
        new_attack[i] = (arr[i-1] + arr[i+1])
        if new_attack[i] > drr[i]:
            stack.append(i)
    new_attack[0] = arr[1]
    new_attack[-1] = arr[-2]
    if new_attack[0] > drr[0]:
        stack.append(0)
    if new_attack[-1] > drr[-1]:
        stack.append(n-1)
    segmax = MaxTree(n)
    segmin = MinTree(n)
    
    # print("drr", drr)
    # print("arr", arr)
    # print("new_attak",new_attack)
    # print("update", update)
    # print(segmax.tree[n:])
    # print(segmin.tree[n:])
    ans = [0] * n
    count = 0
    for round in range(1, n+1):
        # print("-----------------")
        # print("heap", stack, count)

        if n - count <= 1:
            break
        if len(stack) == 0:
            break
        for temp in stack:
            segmax.update(temp, -inf)
            segmin.update(temp, inf)
            count += 1

        ans[round-1] = len(stack)
        if n - count <= 1:
            break
        new_made = set()
        while stack:
            temp = stack.pop()
            left = segmax.query(0, temp)
            right = segmin.query(temp, n)
            if left != -inf:
                new_made.add(left)
            if right != inf:
                new_made.add(right)
        # print("new made", new_made)
        # print("segmax", segmax.tree[n:])
        # print("segmin", segmin.tree[n:])
        # print("newattack", new_attack)
        for cur in new_made:
            left = segmax.query(0, cur)
            right = segmin.query(cur+1, n)
            # print(left, right, cur)
            if left != -inf:
                new_attack[cur] = arr[left]
            else:
                new_attack[cur] = 0
            if right != inf:
                new_attack[cur] += arr[right]
            if new_attack[cur] > drr[cur]:
                stack.append(cur)


    print(*ans)
            
    


for t in range(int(input())):
    solve()