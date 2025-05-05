import sys
input = sys.stdin.readline

def func(a, b, n):
    if n == 1:
        return 1, a
    return (n - 1) * (a - b) + b + 1, (n) * (a - b) + b

def solve():
    q = int(input())
    l = -1
    r = 99999999999999999999999999
    ans = []
    for i in range(q):
        temp_input = list(map(int, input().split()))
        # print("input", temp_input)
        # print("l r", l, r)
        if temp_input[0] == 1:
            new_l, new_r = func(temp_input[1], temp_input[2], temp_input[3])
            if (new_r < l) or (new_l > r):
                # print(0)
                ans.append(0)
            else:
                l = max(new_l, l)
                r = min(new_r, r)
                # print(1)
                ans.append(1)
        elif temp_input[0] == 2:
            a, b = temp_input[1], temp_input[2]
            if a >= r:
                ans.append(1)
                continue
            temp = (r - a) // (a - b)
            if (r - a) % (a - b) != 0:
                temp += 1
            if temp * (a - b) + b < l and temp * (a - b) + a >= r:
                ans.append(temp+1)
            else:
                ans.append(-1)
        # print(l , r)
    print(*ans)
for t in range(int(input())):
    solve()