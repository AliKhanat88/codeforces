def solve():
    n = int(input())

    s_ = list(input())
    r_ = list(input())

    s = s_[:]
    r = r_[:]
    if s[0] != r[0] or s[-1] != r[-1]:
        print(-1)
        return
    done = True
    ans = 0
    for i in range(1, n-1):
        if s[i] != r[i]:
            if s[i-1] == "0":
                need = "1"
            else:
                need = "0"
            if s[i+1] != need and r[i+1] != need:
                s[i+1] = need
            elif s[i+1] == need:
                s[i] = r[i]
            ans += 1
    if done and s[-1] == r[-1]:
        print(ans)
        return

    s = s_[:]
    r = r_[:]
    ans = 0
    for i in range(n-2, 0, -1):
        if s[i] != r[i]:
            if s[i+1] == "0":
                need = "1"
            else:
                need = "0"
            if s[i-1] != need and r[i-1] != need:
                s[i-1] = need
            elif s[i-1] == need:
                s[i] = r[i]
            ans += 1
    if s[0] == r[0]:
        print(ans)
        return
    print(-1)
for t in range(int(input())):
    solve()