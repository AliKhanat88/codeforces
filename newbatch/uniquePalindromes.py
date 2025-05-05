def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    ans = []
    per_a = 0
    per_b = 0
    first = True
    idle = ["a", "y", "z"]
    idle_i = 1
    for i in range(k):
        printer = chr(ord("a") + i)
        if brr[i] - per_b > arr[i] - per_a:
            print("NO")
            return
        if first:
            ac = brr[i] - per_b - 2
            first = False
        else:
            ac = brr[i] - per_b
        for j in range(ac):
            ans.append(printer)
        temp = arr[i] - per_a - ac
        cur = 0
        ac = 0
        while temp > 0:
            if cur >= ac:
                if temp == 0:
                    pass
                if temp == 1:
                    ans.append(idle[idle_i])
                    idle_i = (idle_i + 1) % 3
                    temp -= 1
                elif temp >= 2:
                    ans.append(idle[idle_i])
                    idle_i = (idle_i + 1) % 3
                    ans.append(idle[idle_i])
                    idle_i = (idle_i + 1) % 3
                    temp -= 2
                cur = 0
            else:
                ans.append(printer)
                temp -= 1
                cur += 1
        per_a = arr[i]
        per_b = brr[i]
    print("YES")
    print("".join(ans))
for t in range(int(input())):
    solve()