for t in range(int(input())):
    s = list(input())
    n = len(s)
    if n % 2 == 1:
        s.pop(n//2)
        n -= 1
    if "".join(s) == s[0] * n:
        print("NO")
    else:
        print("YES")
