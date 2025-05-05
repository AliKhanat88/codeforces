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

# def main():
#     arr = [1,2,3]
#     tree = SegTree(arr)
#     print(tree.tree)
#     print(tree.query(0, 2))
#     tree.update(1, 50)
#     print(tree.query(0, 2))

# main()
    
from collections import defaultdict, deque
from heapq import heappop, heappush

# def solve():
def solve(n, m, q, arr, brr, queries):
    # n, m, q = map(int, input().split())
    # arr = list(map(int, input().split()))
    # brr = list(map(int, input().split()))
    # queries = [0] * q
    # for i in range(q):
    #     a, b = map(int, input().split())
    #     queries[i] = (a, b)

    index_ele = defaultdict(lambda:-1)
    for i in range(n):
        index_ele[arr[i]] = i+1

    
    dict_list = defaultdict(lambda: [])

    get_before = SegTree([0] * (m))
    defaulters = set()
    c = 0
    for i in range(m):
        if len(dict_list[brr[i]]) == 0:
            c += 1
            get_before.update(i, 1)
            if get_before.query(0, i+1) != index_ele[brr[i]]:
                defaulters.add(brr[i])
        heappush(dict_list[brr[i]], i)
    # print(c)
    for num in arr:
        # print(num, index_ele[num], len(dict_list[num]),c)
        if len(dict_list[num]) == 0 and index_ele[num] <= c:
            
            defaulters.add(num)
    # print(dict_list)
    ans = []
    print(defaulters)
    if len(defaulters) == 0:
        # print("YA")
        ans.append("YA")
    else:
        # print("TIDAK")
        ans.append("TIDAK")
    for i in range(q):
        a, b = queries[i]
        first = brr[a-1]
        second = b

        brr[a-1] = b
        
        get_before.update(dict_list[first][0], 0)
        if len(dict_list[second]) > 0:
            get_before.update(dict_list[second][0], 0)
        heappush(dict_list[second], a-1)
        while len(dict_list[first]) > 0:
            if brr[dict_list[first][0]] == first:
                get_before.update(dict_list[first][0], 1)
                break
            else:
                heappop(dict_list[first])
        while len(dict_list[second]) > 0:
            if brr[dict_list[second][0]] == second:
                get_before.update(dict_list[second][0], 1)
                break
            else:
                heappop(dict_list[second])
        if get_before.query(0, dict_list[second][0]+1) != index_ele[second]:
            defaulters.add(second)
        if len(dict_list[first]) > 0:
            if get_before.query(0, dict_list[first][0]+1) != index_ele[first]:
                defaulters.add(first)
        else:
            if get_before.query(0, m) >= index_ele[first]:
                defaulters.add(first)
        other_set = set()
        for num in defaulters:
            if len(dict_list[num]) > 0:
                if get_before.query(0, dict_list[num][0]+1) != index_ele[num]:
                    break
                else:
                    other_set.add(num)
            else:
                if get_before.query(0, m) >= index_ele[num]:
                    break
                else:
                    other_set.add(num)
        for num in other_set:
            defaulters.remove(num)
        print(defaulters)
        if len(defaulters) == 0:
            # print("YA")
            ans.append("YA")
        else:
            # print("TIDAK")
            ans.append("TIDAK")
    print(ans)
    return ans
            
            



def main():
    # for t in range(int(input())):
    solve(5,5,10,[1, 2, 3, 4, 5],
[1, 3, 1, 4, 5],
[(4, 4), (5, 1), (4, 2), (2, 2), (1, 5), (4, 4), (4, 4), (1, 1), (1, 4), (2, 2)])
    

            
if __name__ == "__main__":
    main()