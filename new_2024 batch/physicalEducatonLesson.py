from math import sqrt, ceil
def solve():
    n, x = map(int, input().split())

    ans = set() 
    temp1 = n - x 
    temp2 = n + x - 2
    if temp1 % 2 == 0 and temp1 // 2 + 1 >= x:
        ans.add(temp1)
    if temp2 % 2 == 0 and temp2 // 2 + 1 >= x+1:
        ans.add(temp2)
    i = 2
    while i <= ceil(sqrt(temp2)):
        if temp1 % i == 0:
            # print(i)
            if i % 2 == 0 and i // 2 + 1 >= x:
                ans.add(i) 
            if (temp1 // i) % 2 == 0 and (temp1 // i) // 2 + 1 >= x:
                ans.add(temp1 // i)
        if temp2 % i == 0:
            if i % 2 == 0 and i // 2 + 1 >= x+1:
                ans.add(i) 
            if (temp2 // i) % 2 == 0 and (temp2 // i) // 2 + 1 >= x+1:
                ans.add(temp2 // i)
        i += 1
    # print(ans)
    print(len(ans))

for t in range(int(input())):
    solve()