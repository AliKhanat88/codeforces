def solve():
    n, k = list(map(int, input().split()))
    s = input()
    i = 0
    first = None
    while i < len(s):
        if s[i] == "1":
            first = i
            break
        i += 1

    j = n-1
    last = None
    while j >= i:
        if s[j] == "1":
            last = n - j -1
            break
        j -= 1
    count_1 = 0
    for i in range(n):
        if s[i] == "1":
            count_1 += 1
    total = 0
    if last != None and k >= last:
        total -= 10
        k -= last
        # print(k, last, first)
        if first != n - last -1 and k >= first:
            total -= 1
    elif first != None and k >= first:
        total -= 1

    # print(first, last)
    print(total + count_1 * 11)

for t in range(int(input())):
    solve()

    

    