def solve():
    n, k = map(int, input().split())

    s = input()

    bisect = None

    per = s[0]
    count = 0
    for i in range(n):
        if s[i] == per:
            count += 1
        elif s[i] != per:
            if count == k:
                pass
            elif count < k:
                bisect = i
                break
            elif count > k:
                bisect = i - k
                break
            count = 1
            per = s[i]
    if bisect == None:
        bisect = n
    new_s = s[bisect:] + "".join(list(reversed(s[:bisect])))
    # print(new_s)
    per = new_s[0]
    count = 0
    for i in range(n):
        if new_s[i] == per:
            count += 1
        elif new_s[i] != per:
            if count == k:
                pass
            else:
                print(-1)
                return
            count = 1
            per = new_s[i]
    if count > k or count < k:
        print(-1)
        return
    print(bisect)

    




for t in range(int(input())):
    solve()