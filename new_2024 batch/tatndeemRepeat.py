
def solve():
    s = input()

    for i in range(len(s) // 2, 0, -1):
        
        dict = {1: 0, -1:0}
        start = 0
        for j in range(start, i):
            if s[j] == "?" or s[j+i] == "?":
                dict[1] += 1
            elif s[j] == s[j+i]:
                dict[1] += 1
            else:
                dict[-1] += 1
        # print(i, dict)
        if dict[1] == i:
            print(i*2)
            return
        start = 1
        while start + i * 2 <= len(s):
            if s[start-1] != "?" and s[start-1+i] != "?" and s[start-1] != s[start-1+i]:
                dict[-1] -= 1
            else:
                dict[1] -= 1
            if s[start+i-1] != "?" and s[start+i-1+i] != "?" and s[start+i-1] != s[start+i-1+i]:
                dict[-1] += 1
            else:
                dict[1] += 1
            # print(i, start, dict)
            start += 1
            if dict[1] == i:
                print(i*2)
                return
    print(0)
for i in range(int(input())):
    solve()