def print_panaroid_sub(n, arr):
    count = (n * (n + 1)) // 2
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            count -= i
    print(count)
    #hello th

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input()))
    print_panaroid_sub(n, arr)
