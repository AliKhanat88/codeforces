from math import log2
def print_oper(n, arr):
    count = 0 
    max_bits = int(log2(n))
    bit = 1
    while bit <= max_bits:
        bits = 2 ** bit
        half_bits = bits // 2
        # print("bit = ",bits)
        for i in range(0, n-1, bits):
            mini1 = min(arr[i:i+half_bits])
            maxi1 = max(arr[i:i+half_bits])
            mini2 = min(arr[i+half_bits:i+half_bits+half_bits])
            maxi2 = max(arr[i+half_bits:i+half_bits+half_bits])
            # print(arr[i:i+half_bits])
            # print(arr[i+half_bits:i+half_bits+half_bits])
            if maxi2 > mini1 and mini2 < maxi1:
                print(-1)
                return
            elif mini1 > mini2:
                count += 1
        bit += 1
    print(count)   

            
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        print_oper(n, arr)