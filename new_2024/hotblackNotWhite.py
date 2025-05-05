def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    c = [0, 0, 0]
    for num in arr:
        c[num%3] += 1
    ans = []
    if c[0] >= n // 2:
        count = 0
        for num in arr:
            if num % 3 == 0 and count < n // 2:
                ans.append("0")
                count += 1
            else:
                ans.append("1")
        print(2)
        print("".join(ans))
    else:
        count = n // 2 - c[0]
        for num in arr:
            if num % 3 == 0:
                ans.append("0")
            else:
                if count > 0:
                    ans.append("0")
                    count -= 1
                else:
                    ans.append("1")
        print(0)
        print("".join(ans))

solve()