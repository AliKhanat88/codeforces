import sys
input = lambda : sys.stdin.readline().strip()
from collections import deque

def solve():

    n = int(input())
    parent = [0] * n
    
    dq = deque()
    can = True
    for i in range(2, n):
        if can:
            print(f"? {i} {1}", flush=True)
            temp = input()
            if temp == "-1":
                exit()
            if temp == "0":
                parent[i] = 1
                dq.append(i)
                can = False
            else:
                parent[i] = 0
                dq.append(i)
            continue
        while True:
            cur = dq[0]
            print(f"? {i} {cur}", flush=True)
            temp = input()
            if temp == "-1":
                exit()
            if temp == "0":
                parent[i] = cur
                dq.append(i)
                dq.popleft()
                break
            else:
                dq.popleft()
        
    print(f"!", *parent[1:], flush=True)
    


for t in range(int(input())):
    solve()