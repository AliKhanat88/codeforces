from pprint import pprint

def solve():
    n, q = map(int, input().split())

    arr = list(map(int, input().split()))

    bit_arr = [[0 for i in range(21)] for i in range(21)]

    for i , num in enumerate(arr):
        per = 0
        for j in range(21):
            if arr[i] & (2**j) == 0:
                bit_arr[j][j] += ((2**j) - per)
            for k in range(j+1, 21, 1):
                if arr[i] & (2**k) == 0:
                    bit_arr[j][k] += (2**j)
                elif arr[i] & (2**k) == 1 and arr[i] & (2**j) != 1:
                    bit_arr[j][k] += ((2**j) - per)
            # if j < 5:
            #     print(num, j, per)
            per += (num & (2**j))
    
    print(bit_arr)

    for i in range(q):
        k = int(input())
        j = 20
        ans = 0
        while j > -1:
            if bit_arr[j][j] <= k:
                ans += (2 ** j)
                k -= bit_arr[j][j]
                break
            j -= 1
        if j == -1:
            print(ans)
            continue
        j = j - 1
        while j > -1:
            while j > - 1:
                if bit_arr[j][j] <= k:
                    

solve()