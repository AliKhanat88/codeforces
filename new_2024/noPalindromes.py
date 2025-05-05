import sys
input = sys.stdin.readline

def isPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i -1]:
            return False
    return True

def solve():
    s = input().strip()
    if not isPalindrome(s):
        print("YES")
        print(1)
        print(s)
        return
    
    n = len(s)
    for i in range(1, n):
        if s[i] != s[0] and s[i-1] != s[0]:
            print("YES")
            print(2)
            print(s[:i], s[i:])
        
            return
    
    per = None
    count = 0
    for i in range(n):
        # print(i, count)
        if s[i] == s[0]:
            count += 1
        else:
            if per == None:
                per = count
            else:
                if count != per:
                    print("YES")
                    print(2)
                    print(s[:i], s[i:])
                    return
            count = 0
    
    
    per = None
    count = 0
    for i in range(n):
        # print(i, count)
        if s[i] == s[0]:
            count += 1
        else:
            if per == None:
                per = count
            else:
                if count > 1:
                    print("YES")
                    print(2)
                    print(s[:i-1], s[i-1:])
                    return
            count = 0
    
    seti = set()
    for i in range(n):
        seti.add(s[i])
        if len(seti) > 2:
            if not isPalindrome(s[:i+1]) and not isPalindrome(s[i+1:]):
                print("YES")
                print(2)
                print(s[:i+1], s[i+1:])
                return
    seti = set()
    for i in range(n-1, -1, -1):
        seti.add(s[i])
        if len(seti) > 2:
            if not isPalindrome(s[i-1:]) and not isPalindrome(s[:i-1]):
                print("YES")
                print(2)
                print(s[:i-1], s[i-1:])
                return
    print("NO")
        



for t in range(int(input())):
    solve()