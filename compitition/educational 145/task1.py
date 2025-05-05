from collections import defaultdict
for t in range(int(input())):
    stri = input()
    s = defaultdict(lambda:0)
    for i in range(len(stri)):
        s[stri[i]] += 1
    keys = list(s.keys())
    # print(keys)
    # print(s)
    if len(s) == 1:
        print(-1)
    elif len(s) == 2 and (s[keys[0]] == 3 or s[keys[1]] == 3):
        print(6)
    else:
        print(4)


    
    

    