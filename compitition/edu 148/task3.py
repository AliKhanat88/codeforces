def print_min(n, arr):
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            increase = True
            break
        elif arr[i+1] < arr[i]:
            increase = False
            break
    count = 1
    # print(increase)
    while i < n-1:
        if arr[i] > arr[i+1] and increase == False:
            count += 1
            increase = True
            i -= 1
        elif arr[i] < arr[i+1] and increase == True:
            count += 1
            increase = False
            i -= 1
        i += 1
    print(count)
for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 1:
        print(1)
    else:
        print_min(n, arr)