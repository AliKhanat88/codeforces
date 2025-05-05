import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input()
    t = input()

    prefix_s = [0] * (n + 1)
    for i in range(1, n+1):
        if s[i-1] == "1":
            prefix_s[i] += prefix_s[i-1] + 1
        else:
            prefix_s[i] += prefix_s[i-1]
    
    # print("TEST")
    # print(s)
    # print(t)
    # print(prefix_s)
    
    prefix11 = [0] * (n + 1)
    
    for i in range(n-2):
        if t[i] == t[i+2] == "1" and s[i+1] == "0":
            prefix11[i+1] = prefix11[i] + 1
        else:
            prefix11[i+1] = prefix11[i]
    
    prefix10 = [0] * (n + 1)
    
    for i in range(n-3):
        if t[i] == "1" and t[i+2]== "0" and s[i+1] == "0" and s[i+3] == "0":
            prefix10[i+1] = prefix10[i] + 1
        else:
            prefix10[i+1] = prefix10[i]

    prefix01 = [0] * (n+1)

    for i in range(1, n-2):
        if t[i] == "0" and t[i+2] == "1" and s[i+1] == "0" and s[i-1] == "0":
            prefix01[i+1] = prefix01[i] + 1
        else:
            prefix01[i+1] = prefix01[i]
    
    prefix00 = [0] * (n + 1)

    for i in range(1, n - 3):
        if t[i] == "0" and t[i+2] == "0" and s[i-1] == "0" and s[i+1] == "0" and s[i+3] == "0":
            prefix00[i+1] = prefix00[i] + 1
        else:
            prefix00[i+1] = prefix00[i]

    # print(prefix11)
    # print(prefix10)
    # print(prefix01)
    # print(prefix00)

    for i in range(int(input())):
        l, r = map(int, input().split())
        ans = (prefix_s[r] - prefix_s[l - 1])
        if r - l + 1 > 2:
            ans += (prefix11[r-2] - prefix11[l-1])
        if r - l + 1 > 3:
            ans += (prefix10[r-3] - prefix10[l-1])
            ans += (prefix01[r-2] - prefix01[l])
        
        if r - l + 1 > 4:
            ans += (prefix00[r-3] - prefix00[l])

        print(ans)


for t in range(int(input())):
    solve()