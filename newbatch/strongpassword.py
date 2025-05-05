def solve():
    s = input()
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            for j in range(26):
                if chr(ord("a") + j) != s[i]:
                    print(s[:i] + chr(ord("a") + j) + s[i:])
                    return
    for j in range(26):
        if chr(ord("a") + j) != s[-1]:
            print(s + chr(ord("a") + j))
            return


for t in range(int(input())):
    solve()