def solve():
    s = input()
    per = -1
    cost = 0
    for i in range(len(s)):
        if s[i] == "0":
            if i != per+1:
                cost = cost + i - per
            per = per + 1
    print(cost)

for t in range(int(input())):
    solve()