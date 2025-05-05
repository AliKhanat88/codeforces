import sys
input = sys.stdin.readline


def solve():
    l, r, i, k = map(int, input().split())
    ans = 0
    for i in range(1, 61):
        
        cur_xor = 0
        temp_l = l % (2 ** (i + 1))
        if temp_l >= 2 ** i and temp_l % 2 == 0:
            cur_xor = 2 ** i
        temp_r = r % (2 ** (i + 1))
        if temp_r >= 2 ** i and temp_r % 2 == 0:
            cur_xor = cur_xor ^ (2 ** i)
        print(temp_l, temp_r, 2 ** i)
        ans += cur_xor
    l_one = l // 2
    if r % 2 == 1:
        r_one = (r // 2) + 1
    else:
        r_one = (r // 2)
    if l_one % 2 != r % 2:
        ans += 1
    print(ans)


for t in range(int(input())):
    solve()