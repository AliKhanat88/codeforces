for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    i = 0
    k = n-1
    sumi = 0
    while i < k:
        sumi += arr[k] - arr[i]
        k -= 1
        i += 1
    print(sumi)