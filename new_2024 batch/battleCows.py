def solve():
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))
    # print(arr,k)
    temp_arr = arr.copy()
    temp_k = k
    temp = 0
    for i in range(n):
        if arr[i] > arr[k-1]:
            temp = i
            break
    ans2 = 0
    arr[temp], arr[k-1] = arr[k-1], arr[temp]
    k = temp
    per = arr[0]
    for i in range(1, n):
        per = max(arr[i], per)
        if i >= k:
            if arr[k] >= per:
                ans2 += 1
            else:
                break
        # print(per, ans2)

    
    
    if temp_arr[temp_k-1] - temp_arr[0] >= temp_arr[temp_k-1] - temp_arr[1]:
        temp_arr[0], temp_arr[temp_k-1] = temp_arr[temp_k-1], temp_arr[0]
        temp_k = 0
    else:
        temp_arr[1], temp_arr[temp_k-1] = temp_arr[temp_k-1], temp_arr[1]
        temp_k = 1

    ans1 = 0
    for i in range(n):
        if i != temp_k:
            if temp_arr[i] < temp_arr[temp_k]:
                ans1 += 1
            else:
                break
    print(max(ans1, ans2))
for t in range(int(input())):
    solve()