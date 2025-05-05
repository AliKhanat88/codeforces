def solve():
    n = int(input())
    s = list(input())

    ans = 0
    check = "mapie"
    for i in range(n-5+1):
        isFound = True
        for j in range(len(check)):
            if s[i+j] != check[j]:
                isFound = False
        if isFound:
            ans += 1
            s[i+2] = -1
    
    check = "map"
    for i in range(n-3+1):
        isFound = True
        for j in range(len(check)):
            if s[i+j] != check[j]:
                isFound = False
        if isFound:
            ans += 1
            s[i+1] = -1

    check = "pie"
    for i in range(n-3+1):
        isFound = True
        for j in range(len(check)):
            if s[i+j] != check[j]:
                isFound = False
        if isFound:
            ans += 1
            s[i+1] = -1
    print(ans)
for i in range(int(input())):
    solve()