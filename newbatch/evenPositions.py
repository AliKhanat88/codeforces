def solve():
    n = int(input())
    s = input()
    stack = []
    temp1 = s.count("(")
    temp2 = s.count(")")
    ans = 0 
    if temp1 >= temp2:
        count2 = (n // 2 - (temp1 - temp2)) // 2 + (temp1 - temp2)
        count1 = n // 2 - count2
    else:
        count1 = (n // 2 - (temp2 - temp1)) // 2 + (temp2 - temp1)
        count2 = n // 2 - count1
    # print(count1, count2)
    for i in range(n):
        if s[i] == "(":
            stack.append(i)

        elif s[i] == ")":
            ans = ans + i - stack.pop()
        else:
            if len(stack) >= 1 and count2 >= 1:
                ans = ans + i - stack.pop()
                count2 -= 1
            else:
                stack.append(i)
                count1 -= 1
    print(ans)
            


for t in range(int(input())):
    solve()