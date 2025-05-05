import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [0] * n
    for i in range(n):
        a, b = map(int, input().split())
        arr[i] = (a, b)
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            mini = min(arr[i], arr[j])
            maxi = max(arr[i], arr[j])
            if mini[1] >= maxi[0]:
                pairs.append((min(arr[i][0], arr[j][0]), max(arr[i][1], arr[j][1])))
    
    pairs.sort(key= lambda x: x[1])
    
    count = 0
    per = (-1, -1)
    for i in range(len(pairs)):
        if pairs[i][0] > per[1]:
            count+=1
            per = (pairs[i][0], pairs[i][1])
    print(n - count * 2)


for t in range(int(input())):
    solve()