from math import log2

def solve():
    xor = int(input())
    sumi = xor * 2
    n = int(log2(sumi)) + 1
    a = 0
    b = 0
    carry = 0
    need_carry = []
    for i in range(n):
        bit1 = (xor & (2 ** i))
        bit2 = (sumi & (2 ** i))
        # print(bit1, bit2, i)
        if bit1 == 0 and bit2 == 0:
            if carry == 1:
                print(-1)
                return
        elif bit1 == 0 and bit2 != 0:
            if carry == 0:
                need_carry.append(i)
            carry = 0
        elif bit1 != 0 and bit2 == 0:
            if carry == 0:
                need_carry.append(i)
            a += 2 ** i
            carry = 1
        elif bit1 != 0 and bit2 != 0:
            if carry == 1:
                a += 2 ** i
                b += 2 ** i
            else:
                a += 2 ** i
    for num in need_carry:
        a += 2 ** (num-1)
        b += 2 ** (num-1)
    # # print(need_carry)
    # print(a, b)
    if (a+b) // 2 == xor and int(a) ^ int(b) == xor and a % 1 == 0 and b % 1 == 0:
        print(a, b)
    else:
        print(-1)

for t in range(int(input())):
    solve()