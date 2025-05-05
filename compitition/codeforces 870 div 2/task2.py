def print_max(n, arr):
    per = None
    i = 0
    k = n-1
    for i in range(n):
        if i > k:
            break
        if arr[i] != arr[k]:
            temp = max(arr[i], arr[k]) - min(arr[i], arr[k])
            if temp != per and per != None:
                print(1)
                return
            else:
                per = temp
        k -= 1 
    if per == None:
        print(0)
    else:
        print(per)

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print_max(n, arr)