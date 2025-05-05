import sys
input = sys.stdin.readline
from collections import defaultdict

def print_min(n, m , arr):
    pairs_count = [0] * n
    arr_pairs = defaultdict(lambda: [])
    for i in range(m):
        a1, a2 = map(int, input().split())
        pairs_count[a1-1] +=1
        pairs_count[a2-1] +=1
        arr_pairs[a1-1].append(a2-1)
    if m % 2 == 0:
        print(0)
        return
    mini = 9999999999999999999
    for i in range(n):
        if arr[i] < mini and pairs_count[i] % 2 == 1:
            mini = arr[i]
        else:
            for pair in arr_pairs[i]:
                if pairs_count[pair] % 2 == 0 and pairs_count[i] % 2 == 0:
                    if arr[pair] + arr[i] < mini:
                        mini = arr[pair] + arr[i]
    if mini != 9999999999999999999:
        print(mini)

    # print(pairs_count)
for i in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print_min(n, m , arr)