for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    if k % 2 == 0:
        target = "0"
    else:
        target = "1"
    output_str = list(s)
    output_arr = [0] * n
    i = 0
    while i < n-1:
        if s[i] == target:
            if k > 0:
                k -= 1
                output_arr[i] += 1
                output_str[i] = "1"
            else:
                output_str[i] = "0"
        else:
            output_str[i] = "1"
        i += 1
    if k % 2 == 1 and s[n-1] == target:
        output_str[n-1] = "1"
    elif k%2 == 1 and s[n-1] != target:
        output_str[n-1] = "0"
    elif k % 2 == 0 and s[n-1] != target:
        output_str[n-1] = "1"
    else:
        output_str[n-1] = "0"
    output_arr[n-1] = k

    print("".join(output_str))
    print(" ".join(str(num) for num in output_arr))
