import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    s = input()
    
    bit_arr = [[0 for i in range(n+1)] for i in range(31)]
    bit_xor = [[0, 0] for i in range(31)]
    # print(arr)
    # print(s)
    for i, num in enumerate(arr):
        j = 0
        while j < 31:
            # print(i, j, num & (2**j))
            if num & (2 ** j) != 0:
                bit_arr[j][i+1] = 1 + bit_arr[j][i]
            else:
                bit_arr[j][i+1] = bit_arr[j][i]
            if num & (2 ** j) != 0:
                if s[i] == "1":
                    bit_xor[j][1] += 1
                else:
                    bit_xor[j][0] += 1
            j += 1


    # print(bit_arr)
    for i in range(31):
        bit_xor[i][0] = bit_xor[i][0] % 2
        bit_xor[i][1] = bit_xor[i][1] % 2

    # print(bit_xor)
    q = int(input())
    for i in range(q):
        temp = list(map(int, input().split()))
        # print(temp)
        if temp[0] == 1:
            for i in range(31):
                if (bit_arr[i][temp[2]] - bit_arr[i][temp[1]-1]) % 2 == bit_xor[i][0]:
                    bit_xor[i][0] = 0
                else:
                    bit_xor[i][0] = 1
                if (bit_arr[i][temp[2]] - bit_arr[i][temp[1]-1]) % 2 == bit_xor[i][1]:
                    bit_xor[i][1] = 0
                else:
                    bit_xor[i][1] = 1
        else:
            ans = 0
            for i in range(31):
                if bit_xor[i][temp[1]] == 1:
                    ans += (2 ** i)
            print(ans, end=" ")
    print()

for t in range(int(input())):
    solve()