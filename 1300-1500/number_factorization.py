def solve():
    n = int(input())
    temp = n
    arr = [1] * 35
    i = 2
    while i <= temp**(1/2):
        k = 0 
        while temp % i == 0:
            arr[k] *= i
            k += 1
            temp = temp // i
        i += 1
    arr[0] *= temp
    sumi = 0
    for i in range(35):
        if arr[i] != 1:
            sumi += arr[i]

    print(sumi)
            


for t in range(int(input())):
    solve()