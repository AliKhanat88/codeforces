def solve():
    n = int(input())
    i = 2
    ans = ""
    isTrue = True
    while i <= n:
        if isTrue:
            ans += "AA"
        else:
            ans += "BB"
        isTrue = not isTrue
        i += 2
    if n % 2 == 1:
        print("NO")
        return
    print("YES")
    print(ans)
    
for i in range(int(input())):
    solve()