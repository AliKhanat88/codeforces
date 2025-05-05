def print_min(s):
    if s == "_":
        print(2)
        return
    elif s == "^":
        print(1)
        return
    else:
        cost = 0
        per = "_"
        for i in range(len(s)):
            if per == "_" and s[i] == "_":
                cost += 1
            per = s[i]
        if s[-1] == "_":
            cost += 1
        print(cost)


for t in range(int(input())):
    s = input()
    print_min(s)