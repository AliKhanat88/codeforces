def solve():
    s = list(input())   
    k = int(input())

    a = len(s)
    while a < k:
        k -= a
        a -= 1
    # print("TEST")
    # print(s)
    # print(a)
    # print(k)

    stack = []
    temp = len(s) - a
    i = 0
    while i < len(s):
        while len(stack) != 0 and temp > 0:
            if s[i] < stack[-1]:
                stack.pop()
                temp -= 1
            else:
                break
        stack.append(s[i])
        i += 1
    print(stack[k-1], end="")




for t in range(int(input())):
    solve()