def print_per(n, arr):
    r = ""
    i = 0
    n -= 1
    is_done = False
    
    if n == 1:
        print(arr[0], 0)
        return
    while i < n-1:
        if int(arr[i]) < int(arr[i+1]):
            r += f"{arr[i]} 0 "
            is_done = True
            break
        else:
            r += f"{arr[i]} "
        i += 1
    i = i+1
 
    while i < n-1:
        if int(arr[i]) > int(arr[i+1]):
            r += f"{arr[i+1]} "
        else:
            r += f"{arr[i]} "
        i += 1
    if is_done == False:
        r += f"{arr[-1]} 0"
    else:
        r += f"{arr[-1]}"
    print(r)
 
for t in range(int(input())):
    n = int(input())
    arr = input().split()
    print_per(n, arr)