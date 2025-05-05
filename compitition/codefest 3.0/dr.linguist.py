from collections import defaultdict

dict = defaultdict(lambda:0)
s = input()
for i in range(len(s)):
    dict[s[i]] += 1
vals = list(dict.values())
dict2 = defaultdict(lambda:0)
for i in range(len(vals)):
    dict2[vals[i]] += 1

if len(dict2) > 2:
    print("NO")
elif len(dict2) == 2:
    temp = sorted(dict2.items(), key=lambda x:x[1], reverse=True)
    if (temp[1][0] == 1 or temp[1][0] - temp[0][0] == 1) and temp[1][1] == 1:
        print("YES")
    else:
        print("NO")
else:
    print("YES")

