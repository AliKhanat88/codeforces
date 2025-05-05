from collections import defaultdict
import sys
from math import log2

input = sys.stdin.readline


def print_min(s):
    n = len(s)
    chars = list(set(list(s)))
    mini = 999999999999999
    for char in chars:
        maxi = 0
        count = 0
        for j in range(n):
            if s[j] == char:
                if count == 0:
                    continue
                maxi = max(maxi, int(log2(count)) + 1)
                count = 0
            elif j == n-1:
                count += 1
                maxi = max(maxi, int(log2(count)) + 1)
            else:
                count += 1
        mini = min(mini, maxi)

    print(mini)
for t in range(int(input())):
    s = input().rstrip()
    print_min(s)