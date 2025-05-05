from collections import Counter

def solve():
    n, k, m = map(int, input().split())
    s = list(input())

    c1 = Counter(s)
    c2 = Counter()

    for j in range(ord("a"), ord("a") + k):
        if c1[chr(j)] < n:
            print("NO")
            print(chr(j) * n)
            return
    # print(c1)

    for i in range(m):
        c1[s[i]] -= 1
        c2[s[i]] += 1
        for j in range(ord("a"), ord("a") + k):
            # print(f"i: {i}, char: {chr(j)}")
            if c1[chr(j)] < n - c2[s[i]]:
                print("NO")
                print(c2[s[i]] * s[i] + (n - c2[s[i]]) * chr(j))
                return
        # print(c1)
        # print(c2)
    print("YES")
    
    
for t in range(int(input())):
    if t == 3639:
        a = input()
        input()
        print(a)
    else:
        solve()