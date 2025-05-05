from collections import defaultdict

def print_components(n, s):
    dict = defaultdict(lambda:False)
    count = 0
    stack = [0] * (n)
    top = -1
    for i in range(2*n):
        if s[i] == "(":
            if dict[top+1] == False:
                top += 1
                count += 1
                stack[top] = 1
                dict[top] = True
            else:
                top += 1
                stack[top] = 1
        elif s[i] == ")":
            stack[top] = 0
            dict[top+1] = False
            top -= 1
        # print(i)
        # print(dict)
    print(count)
            

for t in range(int(input())):
    n = int(input())
    s = input()
    print_components(n, s)