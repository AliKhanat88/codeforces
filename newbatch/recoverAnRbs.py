from collections import Counter

def solve():
    s = list(input())
    c = Counter(s)

    if c["?"] <= 1:
        print("YES")

    elif c["("] == len(s) // 2 or c[")"] == len(s) // 2:
        print("YES")
    else:
        c1 = len(s) // 2 - c["("]
        c2 = len(s) // 2 - c[")"]
        done = False
        for i in range(len(s)):
            if s[i] == "?":
                if c1 == 1 and done == False:
                    s[i] = ")"
                    c2 -= 1
                    done = True
                else:
                    if c1 > 0:
                        s[i] = "("
                        c1 -= 1
                    else:
                        s[i] = ")"
                        c2 -= 1
        # print(s)
        stack = []
        for char in s:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
            # If the character is a closing parenthesis
            elif char == ')':
                # Check if the stack is empty (i.e., there is no matching opening parenthesis)
                if not stack:
                    print("YES")
                    return
                # Pop the top of the stack (i.e., remove the last opening parenthesis)
                stack.pop()
        
        # If the stack is empty, all parentheses were matched correctly
        if len(stack) == 0:
            print("NO")
        else:
            print("YES")

for t in range(int(input())):
    solve()