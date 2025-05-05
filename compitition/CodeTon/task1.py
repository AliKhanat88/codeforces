def print_poss(n, arr):
    for i in range(1, n+1):
            if arr[i-1] <= i:
                print("YES")
                return
    print("NO")

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_poss(n, arr)