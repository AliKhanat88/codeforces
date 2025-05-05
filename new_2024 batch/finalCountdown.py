def solve():
    n = int(input())

    arr = list(input())

    sum_arr = [0] * (n+1)

    for i in range(n):
        sum_arr[i+1] = sum_arr[i] + int(arr[i])

    carry = 0
    for i in range(n, 0, -1):
        arr[i-1] = str((carry + sum_arr[i]) % 10)
        carry = (carry + sum_arr[i]) // 10
    
    if carry != 0:
        print(carry, end="")
        print("".join(arr))
    else:
        i = 0
        while i < n:
            if arr[i] == "0":
                i += 1
            else:
                break
        print("".join(arr[i:]))
for t in range(int(input())):
    solve()