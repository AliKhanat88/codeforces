import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    for j in range(m):
        s = input().strip()
        # print(len(s), len(arr))
        if len(s) == len(arr):
            dict = defaultdict(lambda: -1)
            done = False
            for i, char in enumerate(s):
                if dict[char] == -1:
                    dict[char] = arr[i]
                else:
                    if dict[char] != arr[i]:
                        print("NO")
                        done = True
                        break
            if done == False:
                vals = sorted(list(dict.values()))
                # print(vals)
                for i in range(1, len(vals)):
                    if vals[i] == vals[i-1]:
                        print("NO")
                        done = True
                        break
            if done == False:
                print("YES")


        else:
            print("NO")
for t in range(int(input())):
    solve()