
    
def solve():
    n, a, b = map(int, input().split())
    
    s = input()
    
    def check(x):
        match = s[:x]
        stack = []
        seti = set()
        count = 0
        # print(match)
        for char in s:
            # print(char, stack)
            if char == match[len(stack)]:
                stack.append(char)
                seti.add(char)
            else:
                if len(seti) > 1 or len(stack) == 0:
                    stack = []
                    seti = set()
                else:
                    if stack[-1] == char:
                        pass
                    else:
                        stack = []
                        seti = set()
            if len(stack) >= x:
                count += 1
                stack = []
                seti = set()
        # print(count, x)
        if count >= b:
            return True
        else:
            return False

    # check(2)
    l = 1
    r = n
    while l+1 < r:
        m = (l + r) // 2
        temp = check(m)
        if temp:
            l = m
        else:
            r = m - 1
    if check(r):
        print(r)
    elif check(l):
        print(l)
    else:
        print(0)
    
    



for t in range(int(input())):
    solve()