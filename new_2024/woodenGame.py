import sys
input = sys.stdin.readline

def solve():
    k = int(input())
    # print("k", k)
    bits = [0] * 21
    for i in range(k):
        num = int(input())
        # print(num)
        temp = input()
        # print(temp, num)
        for bit in range(20, -1, -1):
            if num & (2 ** bit) != 0:
                if bits[bit] == 0:
                    bits[bit] = 1
                else:
                    for j in range(bit - 1, -1, -1):
                        bits[j] = 1
                    break
    ans = 0
    for bit in range(21):
        if bits[bit] == 1:
            ans += (2 ** bit)
    print(ans)


for t in range(int(input())):
    solve()