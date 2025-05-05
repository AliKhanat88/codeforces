import sys
input = sys.stdin.readline


def solve():
    s = [int(x) for  x in list(input().strip())]
    
    def check(i):
        if len(s) - i < 4:
            return False
        if s[i] == 1 and s[i + 1] == 1 and s[i + 2] == 0 and s[i + 3] == 0:
            return True
        else:
            return False
    stack = []
    for i in range(len(s)):
        if check(i):
            stack.append(i)
    q = int(input())
    
    for i in range(q):
        a, b = map(int, input().split())
        a -= 1
        s[a] = b
        for j in range(max(0, a - 4), a + 1):
            if check(j):
                stack.append(j)
        while len(stack):
            if not check(stack[-1]):
                stack.pop()
            else:
                break
        if len(stack) > 0:
            print("YES")
        else:
            print("NO")





for t in range(int(input())):
    solve()