#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

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



def solve(arr):
    # Write your code here
    n = len(arr)
    index_arr = [0] * (n+1)
    for i in range(n):
        index_arr[arr[i]] = i
    
    left = [0] * n
    right = [0] * n
    stack = []
    for i in range(n):
        while len(stack) > 0:
            if arr[i] > stack[-1][0]:
                stack.pop()
            else:
                break
        if len(stack) == 0:
            left[i] = -1
        else:
            left[i] = stack[-1][1]
        stack.append((arr[i], i))

    stack = []
    for i in range(n-1, -1, -1):
        while len(stack) > 0:
            if arr[i] < stack[-1][0]:
                stack.pop()
            else:
                break
        if len(stack) == 0:
            right[i] = n
        else:
            right[i] = stack[-1][1]
        stack.append((arr[i], i))
    print(left)
    print(right)
    seg = SegTree([0]*n)
    ans = 0
    remove = [[] for i in range(n+1)]
    for i in range(n-1, -1, -1):
        seg.update(i, 1)
        for num in remove[i]:
            seg.update(num, -1)
        remove[left[i]].append(i)
        ans += seg.query(i, right[i])
    # print(ans)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
