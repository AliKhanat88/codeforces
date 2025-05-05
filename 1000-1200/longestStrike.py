def print_longest_strike(n, k, arr):
    arr.sort()
    maxi = -1
    i = 0
    per = arr[0]
    last = arr[0]
    count = 0
    upper = -1
    bottom = -1
    while i < n:
        if arr[i] == per:
            count += 1
        else:
            if count >= k:
                if per - last > maxi:
                    maxi = per - last
                    bottom = last
                    upper = per
            else:
                last = arr[i]
            if arr[i] != per + 1:
                last = arr[i]
            per = arr[i]
            count = 1
        # print(f"i={i}, last={last}, per={per}, count={count}")
        i += 1
    # print(maxi, per, last)
    if count >= k and per - last > maxi:
        maxi = per - last
        upper = per
        bottom = last
    if maxi != -1:
        print(bottom, upper)
    else:
        print(-1)

    
            


for t in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print_longest_strike(n, k, arr)
