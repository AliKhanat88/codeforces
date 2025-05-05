def solve():
    n = int(input())
    s = list(input())
    t = list(input())
    if s[0] != t[0] or s[-1] != t[-1]:
        print(-1)
        return
    
    per = 0
    topple = [0] * (n+1)
    topple_val = 0
    ans = 0
    for i in range(1, n-1):
        topple_val += topple[i]
        if i > per:
            per = i
        if topple_val % 2 != 0:
            if s[i] == "0":
                s[i] = "1"
            else:
                s[i] = "0"

        if s[i] != t[i]:
            temp = s[i-1] + s[i]
            done = False
            if temp == "01" or temp == "10":
                while per < n-1:
                    if s[per] == s[per+1]:
                        done = True
                        per += 1
                        break
                    per += 1
            elif temp == "11":
                while per < n:
                    if s[per] == "0":
                        done = True
                        break
                    per += 1
            else:
                while per < n:
                    if s[per] == "1":
                        done = True
                        break
                    per += 1
            if done == False:
                print(-1)
                return
            topple_val += 1
            topple[per] = -1
            ans += per - i
            s[i] = t[i]
    print(ans)

for t in range(int(input())):
    solve()