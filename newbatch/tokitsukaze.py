def solve():
    n = int(input())

    s = input()

    count = 1
    oper = 0
    stack = []
    per = s[0]
    cur = 1
    for i in range(1, n):
        if s[i] == per:
            cur += 1
        else:
            if cur % 2 != 0:
                if len(stack) == 0:
                    stack.append(cur)
                else:
                    minus = 0
                    stack2 = stack[:]
                    while len(stack) != 0:
                        if stack[-1] == 2 and len(stack) > 1:
                            minus += 2
                            stack[-2] += 1
                        oper += 1
                        stack.pop(-1)
                    
                    count = count - minus
            else:
                if len(stack) != 0:
                    stack.append(cur)

            count += 1
            cur = 1
            per = s[i]

    if len(stack) != 0 and cur % 2 == 1:
        minus = 0
        stack2 = stack[:]
        while len(stack) != 0:
            if stack[-1] == 2 and len(stack) > 1:
                minus += 2
                stack[-2] += 1
            oper += 1
            stack.pop(-1)


        count = count - minus

    print(oper, count)




for t in range(int(input())):
    solve()