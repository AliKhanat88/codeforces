from collections import defaultdict
import sys
input = sys.stdin.readline

def print_balanced_trees(n):
    arr = list(map(int, input().split()))
    s = input().rstrip()
    vertices = [i + 1 for i in range(n)]
    vertices[0] = -1
    for num in arr:
        vertices[num-1] = -1
    dict = defaultdict(lambda:[0,0])
    for num in vertices:
        if num != -1:
            sumi = 0
            while True:
                if dict[num][1] == 0:
                    if s[num-1] == "W":
                        sumi = sumi + 1
                    else:
                        sumi = sumi -1
                
                dict[num][0] += sumi
                dict[num][1] += 1
                if num == 1:
                    break
                num = arr[num-2]

    count = 0
    for i, val in dict.items():
        if val[0] == 0:
            count += 1
    print(count)
for t in range(int(input())):
    n = int(input())
    print_balanced_trees(n)