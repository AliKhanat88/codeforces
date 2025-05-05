import sys 
input = sys.stdin.readline
def solve():
    n, q = map(int, input().split())
    arr = [*map(int, input().split())]

    sumi_arr = [0] * n
    
    sumi_arr[0] = arr[0]
    for i in range(1, n):
        sumi_arr[i] = sumi_arr[i-1] + arr[i]
    sumi = sumi_arr[-1]

    for i in range(q):
        l, r, k = map(int, input().split())
        if (sumi - (sumi_arr[r-1] - sumi_arr[l-1] + arr[l-1]) + k * (r - l + 1)) % 2 == 1:
            print("YES")
        else:
            print("NO")
for t in range(int(input())):
    solve()