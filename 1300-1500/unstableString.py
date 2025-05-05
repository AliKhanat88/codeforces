def solve():
    s = input()
    n = len(s)
    break_point = []
    i = 0
    while i < n:
        if s[i] != "?":
            break
        i += 1
    j = n-1
    while j > i:
        if s[i] != "?":
            break
        j -= 1
    
    for k in range(i+1, j+1):
        if s[k] == "?" and s[k-1] != "?":
            per = s[k-1]
            per_i = k-1
        elif s[k] != "?" and s[k-1] == "?":
            # print(s[k], per)
            if (k - per_i - 1) % 2 == 0 and s[k] == per:
                break_point.append((k, k - per_i))
            elif (k - per_i - 1) % 2 != 0 and s[k] != per:
                break_point.append((k, k - per_i))
    break_point.append((len(s) , 0))
    # print(break_point)
    start = 0
    sumi = 0
    ans = 0
    per = None
    while len(break_point) != 0:
        cur = break_point.pop(0)
        for i in range(start, cur[0]):
            if s[i] == per and s[i] != "?":
                sumi = 0

            sumi += 1
            ans += sumi
            per = s[i]
        
        start = cur[0]
        sumi = cur[1] -1
        per = None

    print(ans)





for t in range(int(input())):
    solve()