from collections import defaultdict
import sys
input = sys.stdin.readline

dict_ver = defaultdict(lambda:[])

dict_ver = defaultdict(lambda:[])

n = int(input())

for  i in range(n-1):
    a, b = map(int, input().split())
    dict_ver[a].append(b)
    dict_ver[b].append(a)

arr = list(map(int, input().split()))

temp = set(arr)
if len(temp) > 3:
    print("NO")
elif len(temp) == 1:
    print("YES")
    print(1)
elif len(temp) == 2:
    for i in range(1, n+1):
        temp = set()
        for 
