def print_poss(n, arr):
    while len(arr) != 0 and arr[-1] == 0:
        arr.pop(-1)
    if len(arr) == 0:
        print("YES")
        return
    if arr[0] < 0 or arr[-1] > 0:
        print("NO")
        return
    n = len(arr)
    temp_arr = [1] * n
    temp_arr[-1] = arr[-1]
    temp_arr[-2] = - temp_arr[-1]
    for i in range(n-2, 0, -1):
        diff = temp_arr[i] - arr[i]
        if diff <= 0:
            print("NO")
            return
        diff -= 1
        temp_arr[i-1] += diff
        temp_arr[i] = arr[i]
        
    if temp_arr[0] == arr[0] and sum(arr) == 0:
        print("YES")
    else:
        print("NO")

        

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_poss(n, arr)