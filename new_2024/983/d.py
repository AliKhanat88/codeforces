import sys
input = sys.stdin.readline
from random import randint
 
from bisect import bisect_right, bisect_left
 
def foo(a,k):
    out = 0
    ll,rr=-1,-1
    for l in range(len(a)):
        r = bisect_right(a,a[l]+k)
        if r-l >= out:
            out = r-l
            ll,rr = l,r
    return out,ll,rr

def solve(n, k, a):
    a.sort()
    o,l,r = foo(a,k)
    print(o, l, r)
    na = [a[i] for i in range(n) if not(l<= i < r)]
    o1,_,_ = foo(na,k)
    o3,_,_ = foo(a,2*k+1)
 
    # print(max(o3,o+o1))
    return max(o3,o+o1)
 

 
 
# for i in range(int(input().strip())):
#     n,k = map( int , input().strip().split() )
#     a = list( map( int , input().strip().split() ) )
#     input()
#     solve(n, k, a)



import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n: int, idx_comp = None , str_protocol = False) -> None:
        self.tree = [float('-inf')]*(2*n)
        self.n = n
        self.str_protocol = str_protocol
        if idx_comp is not None:
            self._idx_hash(idx_comp)


    def _idx_hash(self,arr):
        self.idx = {}
        for i in range(self.n):
            v = arr[i]
            if self.str_protocol:
                v = str(v)
            self.idx[v] = i

    def _get_index(self,i: int) -> int:
        if hasattr(self,'idx'):
            if self.str_protocol:
                i = str(i)
            if i not in self.idx:
                raise IndexError
            i = self.idx[i]

        if i >= self.n or i < -1:
            raise IndexError
        return i

    def sum(self,l: int , r: int) -> int:
        l = self._get_index(l) + self.n
        r = self._get_index(r) + self.n

        mx = float('-inf')
        while l <= r:
            if l&1 == 1:
                mx = max(mx , self.tree[l])

                l += 1
            if r&1 == 0:
                mx = max(mx , self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return mx



    def add(self,i: int , v) -> None:
        i = self._get_index(i) + self.n
        self.tree[i] = max(self.tree[i],v)
        i >>= 1
        while i >= 1:
            self.tree[i] = max(self.tree[2*i],self.tree[2*i+1])
            i >>= 1


from bisect import bisect_right


def brute(n, k, a):
    a.sort()
    ls = []
    seg = SegmentTree(n+1)
    for l in range(len(a)):
        r = bisect_right(a,a[l]+k)
        seg.add(r,r-l)
        ls.append((l,r))

    out = 0
    for l,r in ls:
        out = max(out,r-l+seg.sum(0,l))
        out = max(out,r-l)
    # print(out)
    return out


def check():
    n = 10
    k = 2
    for i in range(10000):
        arr = [randint(1, 10) for i in range(n)]
        if brute(n, k, arr[:]) != solve(n,k,arr[:]):
           print("Found")
           print(arr)
           print(brute(n, k, arr) , solve(n,k,arr))
           break


check()

# solve(10, 2, [1, 3, 7, 1, 3, 4, 5, 7, 5, 7])



