def maximal_and(n , k,arr):
    bits = [0] * 31
    and_ope = arr[0]
    for num in arr:
        and_ope = and_ope & num
        for i in range(31):
            if 2**i >num:
                break
            if num & (2**i) != 0:
                bits[i] += 1
    for i in range(30, -1, -1):
        if bits[i] < n and n-bits[i] <= k:
            and_ope += 2 ** i
            k = k - (n-bits[i])
        # print(bits, k)

    print(and_ope)
for t in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    maximal_and(n ,k ,arr)