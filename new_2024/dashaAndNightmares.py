import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    even_dict = [dict() for i in range(26)]
    odd = []
    for i in range(n):
        s = input().strip()
        if len(s) % 2 == 0:
            st_key = [0] * 26
            c = [0] * 26
            for i in range(len(s)):
                c[ord(s[i]) - ord("a")] += 1
            for i in range(ord("a"), ord("z") + 1):
                if c[i - ord("a")] % 2 == 0:
                    st_key[i - ord("a")] = "0"
                else:
                    st_key[i- ord("a")] = "1"
            st_key = "".join(st_key)
            for i in range(ord("a"), ord("z") + 1):
                if c[i - ord("a")] == 0:
                    even_dict[i - ord("a")][st_key] = even_dict[i - ord("a")].get(st_key, 0) + 1
        else:
            odd.append(s)
            # print(st_key)
    # print(even_dict)
    ans = 0
    for s in odd:
        st_key = [0] * 26
        c = [0] * 26
        for i in range(len(s)):
            c[ord(s[i]) - ord("a")] += 1
        for i in range(ord("a"), ord("z") + 1):
            if c[i - ord("a")] % 2 == 0:
                st_key[i - ord("a")] = "1"
            else:
                st_key[i- ord("a")] = "0"
    
        for i in range(ord("a"), ord("z") + 1):
            if c[i - ord("a")] == 0:
                st_key[i - ord("a")] = "0"
                temp = "".join(st_key)
                ans += even_dict[i - ord("a")].get(temp, 0)
                st_key[i - ord("a")] = "1"

    print(ans)

solve()