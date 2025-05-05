from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    mini1 = None
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            mini1 = i
            break

    mini2 = None
    for j in range(n-2, -1, -1):
        # print(j)
        if arr[j] != arr[j+1]:
            mini2 = n - j - 1
            break
    # print(mini1, mini2)
    if mini1 == None and mini2 == None:
        print(-1)
        return
    mini3 = min(mini1, mini2)
    per = -1
    for i in range(1, n):
        if arr[i] != arr[0]:
            # print(i, per)
            mini3 = min(mini3, i - per - 1)
            per = i
    print(mini3)
        

for t in range(int(input())):
    solve()