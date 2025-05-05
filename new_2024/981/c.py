def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    per_0 = 0
    per_1 = 0

    i = 1
    j = n - 2
    while i < j:
        temp_0 = per_0
        if arr[i] == arr[i-1]:
            temp_0 += 1
        if arr[j] == arr[j+1]:
            temp_0 += 1
        new_per_0 = temp_0
        temp_0 = per_1
        if arr[i] == arr[j+1]:
            temp_0 += 1
        if arr[j] == arr[i-1]:
            temp_0 += 1

        new_per_0 = min(new_per_0, temp_0)
        temp_1 = per_1
        if arr[j] == arr[j+1]:
            temp_1 += 1
        if arr[i] == arr[i-1]:
            temp_1 += 1
        new_per_1 = temp_1
        temp_1 = per_0
        if arr[j] == arr[i-1]:
            temp_1 += 1
        if arr[i] == arr[j+1]:
            temp_1 += 1
        new_per_1 = min(new_per_1, temp_1)



        i += 1
        j -= 1
        per_0 = new_per_0

        per_1 = new_per_1
        # print(per_0, per_1, i, j)
    ans = min(per_0, per_1)
    if n % 2 == 1:
        if arr[n // 2] == arr[n // 2 - 1]:
            ans += 1
        if arr[n // 2] == arr[n // 2 + 1]:
            ans += 1
    else:
        if arr[n // 2] == arr[n // 2 - 1]:
            ans += 1
    print(ans)
for t in range(int(input())):
    solve()