from random import randint
from collections import Counter

def solve():
    c = Counter()
    randi = randint(1, 2 ** 64)
    def get(x):
        return c[x ^ randi]
    
    def update(x):
        c[x ^ randi] += 1

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    
    for num in arr:
        update(num)
    
    counts = []
    for key, val in c.items():
        counts.append(val)
    
    counts.sort(reverse=True)
    # print(counts)
    while len(counts) > 0:
        if counts[-1] <= k:
            k -= counts[-1]
            counts.pop()
        else:
            break
    print(max(1, len(counts)))



for t in range(int(input())):
    solve()