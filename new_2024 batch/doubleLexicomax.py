from collections import Counter

def solve():
    s = input()
    c = Counter(list(s))
    # print("TEST")
    # print(s)
    ans = [0] * len(s)
    start = 0
    last = len(s) - 1
    i = ord("a")
    while i < ord("z") +1:
        if c[chr(i)] % 2 != 0:
            for j in range(c[chr(i)] // 2):
                ans[start] = chr(i)
                ans[last] = chr(i)
                start += 1
                last -= 1 
                c[chr(i)] -= 2
            break
        else:
            for j in range(c[chr(i)] // 2):
                ans[start] = chr(i)
                ans[last] = chr(i)
                start += 1
                last -= 1
                c[chr(i)] -= 2
        i += 1
    # if start > last:
    #     print(ans)
    #     return
    # print("ans before", ans)
    for j in range(i+1, ord("z") + 1):
        if c[chr(j)] == last - start:
            for k in range(c[chr(j)] // 2):
                ans[start] = chr(j)
                ans[last] = chr(j)
                start += 1
                last -= 1
                c[chr(j)] -= 2
            ans[last] = chr(i)
            c[chr(i)] -= 1
            last -= 1
            break
        elif c[chr(j)] != 0:
            ans[last] = chr(i)
            c[chr(i)] -= 1
            last -= 1
            break
    for i in range(ord("a"), ord("z") + 1):
        while c[chr(i)] > 0:
            ans[start] = chr(i)
            c[chr(i)] -= 1
            start += 1
    print("".join(ans))
for t in range(int(input())):
    solve()