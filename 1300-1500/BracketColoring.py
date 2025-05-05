def solve():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print(-1)
        return
    inverted = False
    stack = []
    print_out = [0] * n
    for i, char in enumerate(s):
        if inverted == False:
            if char == "(":
                stack.append(char)
                print_out[i] = "1"
            else:
                if len(stack) == 0:
                    inverted = True
                    stack.append(char)
                    print_out[i] = "2"
                else:
                    stack.pop(-1)
                    print_out[i] = "1"
        else:
            if char == ")":
                stack.append(char)
                print_out[i] = "2"
            else:
                if len(stack) == 0:
                    inverted = False
                    stack.append(char)
                    print_out[i] = "1"
                else:
                    stack.pop(-1)
                    print_out[i] = "2"
    if len(stack) != 0:
        print(-1)
        return
    if len(set(print_out)) == 1:
        print(1)
        print("1 " * n)
    else:
        print(2)
        print(" ".join(print_out))


for t in range(int(input())):
    solve()