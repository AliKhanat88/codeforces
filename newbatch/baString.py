def recur(s,k, x, ans):
    if x <= 0:
        ans.append(s)
        return
    org_x = x
    per = 1
    last = None
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "a" and last != None:
            total_b = (last - i) * k
            if org_x // per <= total_b:
                add_b = org_x // per
                ans.append(s[:i+1])
                for j in range(add_b):
                    ans.append("b")
                x = org_x - add_b * per 
                recur(s[last+1:], k, x, ans)
                return
            else:
                per = total_b * per + per
            last = None
        elif s[i] == "*" and last != None:
            pass
        elif s[i] == "*" and last == None:
            last = i
    if last != None:
        total_b = (last + 1) * k
        if org_x // per <= total_b:
            add_b = org_x // per
            for j in range(add_b):
                ans.append("b")
            x = org_x - add_b * per 
            recur(s[last+1:], k, x, ans)
            return


def solve():
    n, k, x = map(int, input().split())
    s = input()
    ans = []
    recur(s,k,x - 1, ans)
    ans = "".join(ans)
    for i in range(len(ans)):
        if ans[i] != "*":
            print(ans[i], end="")
    print()
    # print(ans)
for t in range(int(input())):
    solve()