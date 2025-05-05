def print_operation(n, arr):
    operat = [0] * n
    for i in range(n-1, -1, -1):
        count = 0
        while arr[i] != i+1:
            temp = arr.pop(i)
            count += 1
            arr = [temp] + arr
        # print(arr)
        if count != 0:
            operat[i] = i + 1 - count
    print(" ".join(str(num) for num in operat))
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_operation(n, arr)