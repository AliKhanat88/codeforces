def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n > 2:
        print("NO")
    elif arr[0] + 1 == arr[1]:
        print("NO")
    else:
        print("YES")
        

for t in range(int(input())):
    solve()