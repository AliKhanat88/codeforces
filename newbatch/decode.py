from collections import defaultdict
rem = 10 ** 9 + 7
def solve():
    dict = defaultdict(lambda: [])
    s = input()
    per = 0
    dict[0].append(0)
    for i in range(len(s)):
        if s[i] == "1":
            per += 1
        else:
            per -= 1
        dict[per].append(i+1)
    # print(dict)
    ans = 0
    for key, val in dict.items():
        if len(val) == 1:
            continue
        else:
            multi = [0] * len(val)
            per = 0
            for j in range(len(val) - 1, -1, -1):
                per += (len(s) - val[j] + 1)
                multi[j] = per
                
            for j in range(len(val) - 1):
                ans = (ans + (val[j]+1) * (multi[j+1])) % rem
        # print(ans, val)
    print(ans)
for t in range(int(input())):
    solve()