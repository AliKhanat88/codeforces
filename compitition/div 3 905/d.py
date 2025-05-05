from bisect import bisect_right

def solve():
    q = int(input())
    s = input()
    stack = [(int(s[1]), int(s[2]))]
    print("NO")
    holes = 0
    for i in range(1, q):
        s = input()
        a = int(s[1])
        b = int(s[2])
        if s[0] == "+":
            temp = bisect_right(stack, (b, a))
            stack.insert(temp, (a, b))
            if temp != len(stack) or temp != 0:
                if stack[temp-1][1] < stack[temp+1][0]:
                    if stack[temp-1][1] < a and stack[temp+1][0] > b:
                        holes -= 1
                
            
            
        else:


    for i in range(q):


for t in range(int(input())):
    solve()