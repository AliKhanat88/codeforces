def solve():
    a, b = map(int, input().split())

    temp_b = 1

    ans = 0
    while temp_b <= b:
        if (temp_b * temp_b) - temp_b > a:
            break
        if temp_b != 1:
            ans += 1
        ans += ((a - ((temp_b * temp_b) - temp_b)) // (temp_b * temp_b))
        temp_b += 1
    print(ans)

    

    

for t in range(int(input())):
    solve()