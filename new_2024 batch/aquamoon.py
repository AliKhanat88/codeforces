from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    dict = defaultdict(lambda: [0, 0])

    for i in range(n):
        if (i+1) % 2 == 0:
            dict[arr[i]][0] += 1
        else:
            dict[arr[i]][1] += 1

    arr.sort()
    for i, num in enumerate(arr):
        if dict[num][(i+1) % 2] == 0:
            print("NO")
            return
        dict[num][(i+1) % 2] -= 1
    print("YES")
    
for t in range(int(input())):
    solve()