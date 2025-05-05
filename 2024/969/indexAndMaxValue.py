import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    maxi = max(arr)
    ans = []
    for i in range(m):
        temp = input().strip().split()
        a, b = map(int, temp[1:3])
        if temp[0] == "+":
            if maxi >= a and maxi <= b:
                maxi += 1

        else:
            if maxi >= a and maxi <= b:
                maxi -= 1
        ans.append(maxi)
    print(*ans)
for t in range(int(input())):
    solve()