def solve():
    n = int(input())
    s = input()
    per = 0
    sumi = 0
    i = 0
    while i < n:
        if s[i] != s[per]:
            sumi += (2 ** (i-per) - 1) % 998244353
            per = i
        i += 1
    sumi += (2 ** (i-per) - 1) % 998244353
    print(sumi % 998244353)

for t in range(int(input())):
    solve()
