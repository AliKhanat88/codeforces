def solve():
    l, r = map(int, input().split())

    mul = l
    length = 1
    while mul * 2 <= r:
        mul = mul * 2
        length += 1
    ans = 0
    # print(length)
    lower = l
    higher = r
    while lower + 1 < higher:
        mid = lower + (higher - lower) // 2

        if mul // l * mid <= r:
            lower = mid
        else:
            higher = mid - 1

    if mul // l * higher <= r:
        ans += (higher - l + 1)
    else:
        ans += (lower - l + 1)
    # print(higher, lower)
    if length > 1:
        lower = l
        higher = r
        while lower + 1 < higher:
            mid = lower + (higher - lower) // 2

            if (mul // l * mid) // 2 * 3 <= r:
                lower = mid
            else:
                higher = mid - 1

        if (mul // l * higher)  // 2 * 3 <= r:
            ans += ((higher - l + 1) * (length - 1))
        elif (mul // l * lower)  // 2 * 3 <= r:
            ans += ((lower- l + 1) * (length - 1))

    print(length, ans % 998244353)

for t in range(int(input())):
    solve()