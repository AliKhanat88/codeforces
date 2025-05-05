from collections import Counter, defaultdict


def solve():
    s = input()

    dict= defaultdict(lambda: -1)

    for i in range(len(s)):
        dict[s[i]] = i

    order = []

    for i in range(len(s)):
        if i == dict[s[i]]:
            order.append(s[i])

    # print(order)
    c = Counter()
    found = False
    for i in range(len(s)):
        c[s[i]] += 1
        if i == dict[s[i]] and found == False:
            found = True
        elif i == dict[s[i]] and found == True:
            print(-1)
            return
        if found:
            count = 0
            temp_sum = 0
            for chari in order:
                temp_sum += c[chari]
                count += sum(c.values()) - temp_sum
            
            if count == len(s) - i - 1:
                cur = s[:i+1]
                ans = [cur]
                for chari in order:
                    new_cur = []
                    for j in range(len(cur)):
                        if cur[j] != chari:
                            new_cur.append(cur[j])
                    ans.append("".join(new_cur))
                    cur = new_cur
                # print(ans)
                if "".join(ans) == s:
                    print(s[:i+1], "".join(order))
                    return

    print(-1)


for t in range(int(input())):
    solve()