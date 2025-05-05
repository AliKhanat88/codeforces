import sys
input = sys.stdin.readline
from collections import defaultdict

def print_poss(n, pair_set, diction):
    for pair in pair_set:
        can_be = True
        for j in range(1, pair[0]+1):
            if diction[pair[j]] < 2:
                can_be = False
                break
        if can_be == True:
            print("YES")
            return
    print("NO")


for t in  range(int(input())):
    n = int(input())
    pair_set = [0] * n
    diction = defaultdict(lambda:0)
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(1, temp[0]+1):
            diction[temp[j]] += 1
        pair_set[i] = temp
    print_poss(n, pair_set, diction)

