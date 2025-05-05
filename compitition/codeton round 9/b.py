def solve():
    s = input()
    if len(s) == 1:
        print(-1)
        return 
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            print(s[i-1]+s[i])
            return
    for i in range(2, len(s)):
        if s[i] != s[i-1] and s[i] != s[i-2] and s[i-1] != s[i-2]:
            print(s[i-2] + s[i-1]+s[i])
            return
    print(-1)


for t in range(int(input())):
    solve()