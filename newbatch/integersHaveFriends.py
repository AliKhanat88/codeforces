from math import gcd

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)
        
    def build(self, data):
        # Initialize leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = gcd(self.tree[i * 2], self.tree[i * 2 + 1])
            
    def range_gcd(self, left, right):
        # Get GCD in the interval [left, right)
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2:
                result = gcd(result, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                result = gcd(result, self.tree[right])
            left //= 2
            right //= 2
        return result

# # Example usage
# if __name__ == "__main__":
#     data = [2, 3, 6, 9, 5]
#     seg_tree = SegmentTree(data)
#     print(seg_tree.range_gcd(1, 4))  # GCD of range [1, 4) which is GCD(3, 6, 9)
#     print(seg_tree.range_gcd(0, 5))  # GCD of range [0, 5) which is GCD(2, 3, 6, 9, 5)
#     print(seg_tree.range_gcd(2, 3))  # GCD of range [2, 3) which is GCD(6)

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(1)
        return
    new_arr = [0] * (n - 1)
    for i in range(1, n):
        mini = min(arr[i], arr[i-1])
        maxi = max(arr[i], arr[i-1])
        new_arr[i-1] = maxi - mini
        if new_arr[i-1] == 0:
            new_arr[i-1] = maxi
    
    seg_tree = SegmentTree(new_arr)
    per = 0
    cur_gcd = new_arr[0]
    if cur_gcd <= 1:
        maxi = 0
    else:
        maxi = 1
    for i in range(1, len(new_arr)):
        cur_gcd = gcd(cur_gcd, new_arr[i])
        if cur_gcd > 1:
            maxi = max(maxi, i - per + 1)
        else:
            while per <= i and cur_gcd <= 1:
                per += 1
                cur_gcd = seg_tree.range_gcd(per, i+1)
            maxi = max(maxi, i - per + 1)
    print(maxi + 1)
for t in range(int(input())):
    solve()