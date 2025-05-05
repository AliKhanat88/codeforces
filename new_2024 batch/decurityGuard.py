def solve():
    s = list(input())

    stack_count = 0

    i = 0
    found = False
    ans = "1 1"
    while i < len(s):
        if s[i] == "+":
            stack_count += 1
        else:
            if stack_count == 0:
                found = True
                break
            else:
                stack_count -= 1
        i += 1
    if found:
        for j in range(len(s)-1, i, -1):
            if s[j] == "+":
                s[i], s[j] = s[j], s[i]
                ans = f"{i+1} {j+1}"
                break
    stack_count = 0
    i = 0
    while i < len(s):
        if s[i] == "+":
            stack_count += 1
        else:
            if stack_count == 0:
                print(-1)
                return
            else:
                stack_count -= 1
        i += 1
    print(ans)

for t in range(int(input())):
    solve()