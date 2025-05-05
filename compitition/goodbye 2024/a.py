import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # arr.sort()
    for i in range(n):
        for j in range(i+1, n):
            mini = min(arr[i], arr[j])
            maxi = max(arr[i], arr[j])
            if mini + mini > maxi:
                print("YES")
                return
            else:
                break
            
    print("NO")
    
for t in range(int(input())):
    solve()