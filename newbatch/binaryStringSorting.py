import sys
input = sys.stdin.readline

mult = 1000000000001

def solve():
    s = input()
    black = [0] * len(s)
    b_c = 0
    for i in range(len(s)):
        if s[i] == "1":
            b_c += 1
        black[i] = b_c

    white = [0] * len(s)
    w_c = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == "0":
            w_c += 1
        white[i] = w_c
    # print("TEST")
    # print(black)
    # print(white)
    mini = white[0] * mult
    for i in range(1, len(s)):
        if s[i-1] == "1" and s[i] == "0":
            mini = min(mini, (black[i-1] - 1 + white[i] - 1) * mult + mult - 1)
        else:
            mini = min(mini, (black[i-1] + white[i]) * mult)
    print(min(mini, black[-1] * mult))
    
for t in range(int(input())):
    solve()