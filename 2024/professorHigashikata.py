import sys
input = sys.stdin.readline

inf = 999999999999999999

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [inf] * (self.n * 2)
        for i in range(self.n):
            self.tree[i + self.n] = arr[i]
        
        for i in range(self.n -1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])


    def update(self, index, val):
        
        i = index + self.n

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

# def main():
#     arr = [1,2,3]
#     tree = SegTree(arr)
#     print(tree.tree)
#     print(tree.query(0, 2))
#     tree.update(1, 50)
#     print(tree.query(0, 2))

# main()
    

def solve():
    n,m,q = map(int, input().split())
    s = list(map(int, list(input().strip())))
    seq = [i for i in range(1, n+1)]
    tree = SegTree(seq)

    priority = []
    for i in range(m):
        a, b = map(int, input().split())
        temp = tree.query(a-1, b)
        while temp <= n + 5:
            priority.append(temp)
            tree.update(temp-1, inf)

            temp = tree.query(a-1, b)
    # print(s)
    # print(seq)
    # print(priority)

    ones = s.count(1)

    pr_ele = set()
    pr_one = 0
    # print(min(ones, len(priority)))
    for i in range(min(ones, len(priority))):
        if s[priority[i]-1] == 1:
            pr_one += 1
        pr_ele.add(priority[i])
    # print(ones)
    # print(pr_one)
    # print(pr_ele)


    for j in range(q):
        a = int(input())
        if s[a-1] == 1:
            ones -= 1
            s[a-1] = 0
            if a in pr_ele:
                pr_one -= 1
        else:
            ones += 1
            s[a-1] = 1
            if a in pr_ele:
                pr_one += 1
        if ones > len(priority):
            # print(pr_ele)
            print(len(priority)-pr_one)
            continue
        # print(pr_ele)
        if ones > len(pr_ele):
            if s[priority[len(pr_ele)] - 1] == 1:
                pr_one += 1
            pr_ele.add(priority[len(pr_ele)])
        elif ones < len(pr_ele):
            if s[priority[len(pr_ele)-1] - 1] == 1:
                pr_one -= 1
            pr_ele.remove(priority[len(pr_ele) - 1])
        
        print(ones-pr_one)
        
    

solve()