from heapq import heappop, heappush
from collections import defaultdict
import sys
input = sys.stdin.readline

firstHeap = []
lastHeap = []

dictFirst = defaultdict(lambda:0)
dictLast = defaultdict(lambda:0)

for q in range(int(input())):
    check, a, b = input().split()
    # print(a,b)
    if check == "+":
        heappush(firstHeap, -int(a))
        heappush(lastHeap, int(b))
        dictFirst[int(a)] += 1
        dictLast[int(b)] += 1
    else:
        dictFirst[int(a)] -= 1
        dictLast[int(b)] -= 1

    while len(firstHeap) > 0:
        temp1 = -heappop(firstHeap)
        # print(temp1)
        if dictFirst[temp1] > 0:
            heappush(firstHeap, -temp1)
            break

    while len(lastHeap) > 0:
        temp2 = heappop(lastHeap)
        if dictLast[temp2] > 0:
            heappush(lastHeap, temp2)
            break
    if len(firstHeap) <= 0:
        print("NO")
    elif temp2 < temp1:
        print("YES")
    else:
        print("NO")
    
