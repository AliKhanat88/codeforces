def solve():
    n = int(input())
    s = input()
    ans = 0
    isDouble = False
    if s[0] == "1":
        ans += 1
    for i in range(1, n):
        if s[i] == "1" and s[i-1] == "1":
            isDouble = True
        if s[i] == "1":
            ans += 1
    if ans == 2 and isDouble == True:
        print("NO")
    elif ans % 2 == 1:
        print("NO")
    else:
        print("YES")

for t in range(int(input())):
    solve()